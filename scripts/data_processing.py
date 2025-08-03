import re
import unicodedata
from matplotlib import pyplot as plt


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


# Mapeando os códigos:
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


# Bloco de importação protegida:
if __name__ == "__main__":
    user_input = input("Insira o texto: ")
    result = clean_names(user_input)
    print(f"Resultado: {result}")