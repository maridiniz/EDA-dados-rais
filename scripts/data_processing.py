import re
import unicodedata
from ftplib import FTP
import py7zr
import tempfile
import os
import sys
import pandas as pd

# -------------------------------------------------------------------------


# Normalização dos labels das variáveis:
def clean_names(s:str) -> str:
    """Retorna os labels das colunas normalizados."""

    name = s.strip().lower()
    normalized = unicodedata.normalize("NFKD", name)
    name = normalized.encode("ascii", "ignore").decode("ascii")
    name = re.sub(r"[^a-z0-9]+", "_", name)
    if name and name[0].isdigit():
        name = "col_" + name
    
    return name


# --------------------------------------------------------------------------


# Aplicação que realiza ETL do servidor FTP do ministério do trabalho:
def ftp_ingestion(host:str, cwd:str, login="", nrows=None, cols= None) -> pd.DataFrame:
    """Extrai arquivos de um servidor FTP e retorna como objeto DataFrame do pandas."""

    print("Iniciando aplicação...\n")
    
    print("FTP server extracter\n")

    ftp_connection = FTP(host) # Define a conexão com o servidor FTP.

    # Permissão de acesso:
    ftp_connection.login(login) if login else ftp_connection.login()
    
    ftp_connection.cwd(cwd) # Define o diretório dentro do servidor.
    
    # Itera sobre os arquivos no diretório indicado.
    files = [file for file in ftp_connection.nlst() if file.endswith(".7z")]

    if not files:
        raise FileNotFoundError("Nenhum arquivo .7z encontrado.")

    while True: # Loop do menu de seleção de arquivos do diretório.

        print("Esta é a lista de arquivos no diretório indicado: \n")

        # Lista os arquivos disponíveis do diretório:
        for index, file in enumerate(files):
            print(f"Index: {index}, Arquivo: {file}")
        
        user_input = input("Selecione um arquivo digitando seu index.\nPressione (q) para sair: \n").strip().lower()

        if user_input in ["q", "sair", ""]:
            print("Saindo...")
            sys.exit()
        
        print("Extraindo arquivo selecionado do servidor...\n")
        
        try:
            user_reply = int(user_input)
            selected_file = files[user_reply]
        except (ValueError, IndexError):
            print("Opção não encontrada, tente novamente.\n")
            continue


        # Defina um diretório temporário para armazenar arquivo selecionado:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".7z") as temp:
            ftp_connection.retrbinary(f"RETR {selected_file}", temp.write)
            temp_path = temp.name

        # Descompacta arquivo de extensão .7z:
        try:
            with tempfile.TemporaryDirectory() as extracted_dir:
                with py7zr.SevenZipFile(temp_path, "r") as archive:
                    archive.extractall(path=extracted_dir)
                
                # Itera sobre os arquivos descompactados:
                for file in os.listdir(extracted_dir):
                    full_path = os.path.join(extracted_dir, file)
                    if file.endswith((".csv", ".txt")):
                        print("Extração de csv/txt bem sucedida!")
                        df = pd.read_csv(full_path, sep=";", encoding="ISO-8859-1", nrows=nrows, usecols=cols)
                        return df
                    
                    elif file.endswith("json"):
                        df = pd.read_json(full_path)
                        print("Extração de json bem sucedida.")
                        return df
                    else:
                        print("Nenhum arquivo compatível.")
                        raise FileNotFoundError("Arquivo com extensão sem suporte.")
                                           
        finally:
            os.unlink(temp_path)


# --------------------------------------------------------------------------


# Mapeamento dos códigos:
sexo_translation = {
    1: "masculino",
    2: "feminino",
}

faixa_etaria_translation = {
    1: "10 a 14 anos",
    2: "15 a 17 anos",
    3: "18 a 24 anos",
    4: "25 a 29 anos",
    5: "30 a 39 anos",
    6: "40 a 49 anos",
    7: "50 a 64 anos",
    8: "65 anos ou mais",
}

faixa_remun_translation = {
    0: "Até 0,50 salários mínimos",		
    1: "0,51 a 1,00 salários mínimos",		
    2: "1,01 a 1,50 salários mínimos",		
    3: "1,51 a 2,00 salários mínimos",		
    4: "2,01 a 3,00 salários mínimos",	
    5: "3,01 a 4,00 salários mínimos",		
    6: "4,01 a 5,00 salários mínimos",		
    7: "5,01 a 7,00 salários mínimos",		
    8: "7,01 a 10,00 salários mínimos",		
    9: "10,01 a 15,00 salários mínimos",		
    10: "15,01 a 20,00 salários mínimos",		
    11: "Mais 20,00 salários mínimos",	
}

raca_cor_translation = {
    1: "indigena",
    2: "branca",
    4: "preta",
    6: "amarela",
    8: "parda",
    9: "ignorado",
}

escolaridade_translation = {
    1: "analfabeto",
    2: "ate 5.a inc",
    3: "5.a co fund",
    4: "6.a 9.fund",
    5: "fund comp",
    6: "medio incomp",
    7: "medio comp",
    8: "sup. incomp",
    9: "sup. comp",
   10: "mestrado",
   11: "doutorado",
}