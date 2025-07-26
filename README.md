# Análise Exploratória de Dados da RAIS

![Python](https://img.shields.io/badge/Python-3.7%20|%203.8%20|%203.9%20|%203.10-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-brightgreen)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.12.2-blue?logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)
![Static Badge](https://img.shields.io/badge/Numpy-1.26%2B-blue)
![Static Badge](https://img.shields.io/badge/matplotlib-13.9%2B-lightgreen)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)](https://jupyter.org)

---

## Objetivo do projeto

Realizar uma análise exploratória (EDA) da base de dados da RAIS (Ano base 2024) para:
- Analisar distribuições de frequência da faixa salarial média em São Paulo.
- Identificar diferenças salariais por gênero e etnia.
- Investigar a taxa de ocupação por idade e escolaridade.

---

## Configurações do Ambiente

### Pre-requisitos:

- Python 3.9+
- Dependências: `pandas`, `Numpy`, `Matplotlib`, `Seaborn`

### Instalação

1. Instale as dependências:
```python
pip install pandas seaborn matplotlib numpy
```

2. Clone o repositório:
```bash
git@github.com:maridiniz/EDA-dados-rais.git
```

---

## Estrutura do Projeto

```
.
└── 📦 EDA-dados-rais/
    ├── 📂 dados/
    │   └── 📄 dicionario_rais.xls                        # Metadados com a tradução das variáveis.
    ├── 📂 image/
    ├── 📂 script/
    │   └── 🐍📄 exploratory_data_analysis_rais.ipybn     # código fonte.
    ├── 📄 README.md                                      # Visão geral do projeto.
    └── 📄 License                                        # Licença MIT.    
```

---

## Fluxo da Análise

**Carregando os dados**:

Os dados da Rais são geralmente bem grandes, e nesse projeto eles são acessados diretamente do servidor [FTP](ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2024/) do Ministério do Trabalho, através de uma applicação de ETL, que é um dos projetos do meu portfólio, [ingestao-de-dados-ftp](https://github.com/maridiniz/ingestao-de-dados-ftp). Acesse e visualize como é feito processo de extração e carregamento dos arquivos.

**Limpeza e pré-processamento**:

O dataset possui todas as variáveis codificadas em valores numéricos, o que é um padrão dos dados da Rais. Foi realizado o mapeamento dos códigos com base nos [metadados oficiais](/dados), e posteriormente tradução destes dados para realizar a EDA. Decidi manter as variáveis codificadas junto das variáveis já com valores traduzidos, tudo no mesmo dataset `df_sp`. As colunas com dados traduzidos possuem as suas observações discretizadas, ou seja, em dados agrupados em intervalos.

As informações de interesse para este projeto são apenas da cidade de São Paulo, então foi realizada a filtragem por município, resultando em uma base de dados com 283.108 linhas e 

A base de dados, após a filtragem das informações de interesse, não possuem dados faltantes. Foram aplicadas funções para padronizar as colunas do dataset para garantir dados concisos e íntegros.

**Análise exploratória**:

- Técnicas de visualização: 
     - Histograma para obter a distribuição de frequência das faixas salariais e avaliar no contexto de gênero.
     - Violino para visualizar a distribução salarial considerando raça/cor.
- estatísitca descritiva ()

---

## Demonstração
