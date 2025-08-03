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
- Analisar distribuições das faixas médias salariais da cidade de São Paulo.
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
    │   ├── 📄 dicionario_rais.xls     # Metadados oficiais.
    │   └── 📄 dados_processados.csv   # Dados já processados.
    ├── 📂 image/
    ├── 📂 script/
    │   ├── 🐍📄 exploratory_data_analysis_rais.ipybn  # Notebook com o código fonte
    │   └── 📄 data_processing.py    # Módulo com as funções variáveis.
    ├── 📄license
    └── 📄README.md  # Visão geral do projeto. 

```

---

## Fluxo da Análise

**Carregando os dados**:

Os dados da Rais são geralmente bem grandes, e nesse projeto eles são acessados diretamente do servidor [FTP](ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2024/) do Ministério do Trabalho, através de uma applicação de ETL, que é um dos projetos do meu portfólio, [ingestao-de-dados-ftp](https://github.com/maridiniz/ingestao-de-dados-ftp). Acesse e visualize como é feito processo de extração e carregamento dos arquivos.

**Limpeza e pré-processamento**:

O dataset possui todas as variáveis codificadas em valores numéricos, o que é um padrão dos dados da Rais. Foi realizado o mapeamento dos códigos com base nos [metadados oficiais](/dados), e posteriormente foi criado um dicionário com as traduções para inferência, e assim prosseguir com a EDA. Decidi manter as variáveis codificadas junto das variáveis já com valores traduzidos, tudo no mesmo dataset `translated_df_sp`. As colunas com dados traduzidos possuem as suas observações discretizadas, ou seja, em dados agrupados em intervalos/faixas. Foi optado pela transformação do tipo de dado das colunas que apresentavam uma ideia de ordem (Categórica ordinal) para o tipo `Categorical` e assim preservar suas ideias de ordem.

As informações de interesse para este projeto são apenas da cidade de São Paulo, então foi realizada a filtragem por município e também apenas das variáveis de interesse, resultando em uma base de dados com 6.669.537 linhas e 11 variáveis, sendo 6 codificadas — que decidi manter — e 5 traduzidas.

A base de dados, após a filtragem das informações de interesse, não possuem dados faltantes e os outliers são dados válidos. Foram aplicadas funções para padronizar as colunas do dataset para garantir dados concisos e íntegros.

*Nota*:

O módulo [`data_processing.py`](/scripts/data_processing.py) possui as funções user_defined utilizadas neste projeto e o dicionário utilizado na inferência para traduzir os valores das observações.

**Análise exploratória**:

- Técnicas de visualização: 
     - Gráficos de barras para obter a distribuição de frequência das faixas salariais e avaliar no contexto de gênero, assim como a taxa de ocupação de faixa etária e de gênero.
     - Boxplot para ampliar a visão de distribuição das faixas médias salariais.
     - Violino para visualizar a distribução salarial considerando raça/cor.

- Grupos de comparação (gênero, etnia, faixa etária e nível de educação)

---

## Insights e Conclusão

Avaliado a distribuição de acordo com cada faixa salarial na cidade de São Paulo, observamos uma distribuição assimétrica positiva, onde os maiores salários se concentram em poucos indivíduos. 28% dos indivíduos estão na faixa de 1,01 a 1,5 salários mínimos (moda), e 2,2% estão na faixa salarial de até 0,5 salários mínimos, enquanto que indivíduos que recebem a partir de 4 salários mínimos são menos que 5%.
![](/image/distribuicao_faixas_salariais.png)

Agora, avaliando a distribuição salarial, observamos que 25% dos trabalhadores estão abaixo de 1, 01 a 1,50 salários mínimos, enquanto que 25% ganham mais de 4 salários mínimos. A mediana é de 1,51 a 2,00 salários mínimos, o que representa 50% dos nossos salários. A variação dos salários na cidade fica entre 1 a 4 salários mínimos. 
![](/image/boxplot_faixas_salariais.png)

Considerando a distribuição salarial em um contexto de gênero, percebemos que as mulheres são maioria quando os salários são mais baixos, já os homens predominam os salários mais altos. A taxa de ocupação dos homens também é maior em relação as mulheres, mais de 50% e aproximadamente 48% respectivamente.
![](/image/ocupacao_distribuicao_combined.png) 

Já com relação a etnia, vemos que os grupos pardos, pretos, indígenas e amarelos possuem 50% dos indivíduos com uma faixa média salarial de 1,51 a 2,00 salários mínimos, equanto brancos possuem 50% dos seus representantes com uma faixa média salarial de 2,01 a 3,00 salários mínimos. No entanto, avaliando a variabilidade das faixas médias salariais entre os grupos, brancos e amarelos são os que possuem m amior variação. Para brancos, os salários variam entre 1,01 a 1,50 e 4,01 a 5,00 salários mínimos, já os amarelos tem uma variação de 1,01 a 1,50 e 5,01 a 7,00 salários mínimos. Os grupos pardos, pretos e indígenas possuem uma menor variação de salário se comparmos aos dois primeiros grupos citados. A variação vai de 1,01 a 1,50 e 2,01 a 3,00 salários mínimos, e entre esses três grupos, os indígenos apresentam uma maior reresentação nas menores faixas médias salariais, evidencializando uma desigualdade ainda maior neste grupo.
![](/image/violino_raca_cor.png)

As taxas de ocupação considerando faixa etária e escolaridade se mostram da seguinte forma:
- Faixa etária de 18 a 24 e 25 a 29 ambas estão muito próximas quanto a taxa de ocupação, de 16,4% e 16,2% respectivamente.
- Para faixa etária de 30 a 39 e 40 a 49 anos, temos uma taxa de 29% e 22,8% respectivamente.
- Para 50+, temos uma taxa de aproximadamente 15%.
- 54,7% da taxa de ocupação são de pessoas com ensino médio completo.
- menos de 1% é a taxa de ocupação de profissionais com mestrado e doutorado.
- Profissionais com superior completo, compreendem uma taxa de ocupação de 23,4%.
![](/image/taxa_faixa_etaria.png)
![](/image/taxa_escolaridade.png)
