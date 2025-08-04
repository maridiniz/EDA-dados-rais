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
    ├── 📂 image/
    ├── 📂 script/
    │   ├── 🐍📄 exploratory_data_analysis_rais.ipybn  # Notebook com o código fonte
    │   └── 📄 data_processing.py    # Módulo com as funções variáveis.
    ├── 📄license
    └── 📄README.md  # Visão geral do projeto.
    └── 📄.gitignore 

```

---

## Fluxo da Análise

**Carregando os dados**:

Os dados da Rais são geralmente bem grandes, e nesse projeto eles são acessados diretamente do servidor [FTP](ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2024/) do Ministério do Trabalho, através de uma applicação de ETL, que é um dos projetos do meu portfólio, [ingestao-de-dados-ftp](https://github.com/maridiniz/ingestao-de-dados-ftp). Acesse e visualize como é feito processo de extração e carregamento dos arquivos.

**Limpeza e pré-processamento**:

Foi realizado a filtragem apenas das variáveis de interesse, assim como também o município alvo, que no caso é a cidade de São Paulo. As observações das variáveis da base de dados da Rais são codificadas, então foi necessário traduzir essas informações com base nos [`metadados oficiais`](/dados/dicionario_rais.xls). Foi criado um módulo que contém o dicionário com os valores utilizados na tradução, também contém funções utilizadas no pré-processamento dos dados.

Após filtragem e tradução dos dados, o dataset contém 11 variáveis — 6 são as variáveis originais codificadas e 5 são as variáveis com as observações traduzidas — e 6.669.537 linhas. Não foi encontrado indícios de dados faltantes e os outliers encontrados se tratam de dados válidos e que não foram removidos. 

Todas as variáeis de interesse após tradução são do tipo qualitativas, nominais e ordinais. Foi necessário realizar a trasformação das variáveis categóricas ordinais para que fosse preservada a ideia de ordem destes dados.

Foram criados dataset menores com informações específicas para facilitar em algumas técnincas de visualização, como foi o caso do gráfico de barras que obtém a taxa de ocupação por gênero (dataset `taxa_ocupacao_genero`). Outra técnica de visualização onde foi criado outro dataset com informações específicas foi o `distribution_sex` que é utilizado para visualizar a distribuição salarial no contexto de gênero.

**Análise exploratória**:

- Estatística Descritiva: 

Todas as técnicas de estatística descritivas utilizadas foram específicas quando tratamos de dados categóricos, uma vez que não são dados que podemos quantificar com medidas de tendência central como média e de disperção como variância e desvio padrão. No entanto, anda conseguimos utilizar a moda, através das frequências de distribuições com gráficos de barras, ou mediana e intervalo interquartis, nos casos de dados ordinais através dos bloxplots e violinos por exemplo. Algumas das técnicas utlizadas foram:

- Gráficos de barras para avaliar a distribuição salarial no contexto de gênero, assim como as taxas de ocupação por faixa  etária, escolaridade e gênero.
- Boxplot para ampliar a visão de distribuição salarial.
- Violino para visualizar a distribução salarial considerando etnia.

---

## Insights e Conclusão

Avaliado a distribuição de acordo com cada faixa salarial na cidade de São Paulo, observamos uma distribuição assimétrica positiva, onde os maiores salários se concentram em poucos indivíduos. 28% dos indivíduos estão na faixa de 1,01 a 1,5 salários mínimos (moda), e 2,2% estão na faixa salarial de até 0,5 salários mínimos, enquanto que indivíduos que recebem a partir de 4 salários mínimos são menos que 5%.

![](/image/distribuicao_faixas_salariais.png)

Agora, avaliando a distribuição salarial, observamos que 25% dos trabalhadores estão abaixo de 1, 01 a 1,50 salários mínimos, enquanto que 25% ganham mais de 4 salários mínimos. A mediana é de 1,51 a 2,00 salários mínimos, o que representa 50% dos nossos salários. A variação dos salários na cidade fica entre 1 a 4 salários mínimos. Os outliers demonstram que há indivíduos que chegam a faixas médias salariais maiores que 15 salários mínimos.

![](/image/boxplot_faixas_salariais.png)

Considerando a distribuição salarial em um contexto de gênero, percebemos que as mulheres são maioria quando os salários são mais baixos, já os homens predominam os salários mais altos. A taxa de ocupação dos homens também é maior em relação as mulheres, mais de 50% e aproximadamente 48% respectivamente.

![](/image/ocupacao_distribuicao_combined.png) 

Já com relação a etnia, vemos que os grupos pardos, pretos, indígenas e amarelos possuem 50% dos indivíduos com uma faixa média salarial de 1,51 a 2,00 salários mínimos, equanto brancos possuem 50% dos seus representantes com uma faixa média salarial de 2,01 a 3,00 salários mínimos. No entanto, avaliando a variabilidade das faixas médias salariais entre os grupos, brancos e amarelos são os que possuem maior variação. Para brancos, os salários variam entre 1,01 a 1,50 e 4,01 a 5,00 salários mínimos, já os amarelos tem uma variação de 1,01 a 1,50 e 5,01 a 7,00 salários mínimos. Os grupos pardos, pretos e indígenas possuem uma menor variação de salário se comparmos aos dois primeiros grupos citados. A variação vai de 1,01 a 1,50 e 2,01 a 3,00 salários mínimos, e entre esses três grupos, os indígenos apresentam uma maior representação nas menores faixas médias salariais, evidencializando uma desigualdade ainda maior neste grupo.

![](/image/violino_raca_cor.png)

As taxas de ocupação considerando faixa etária e escolaridade se mostram da seguinte forma:
- Faixa etária de 18 a 24 e 25 a 29 ambas estão muito próximas quanto a taxa de ocupação, de 16,4% e 16,2% respectivamente.
- Para faixa etária de 30 a 39 e 40 a 49 anos, temos uma taxa de 29% e 22,8% respectivamente.
- Para 50+, temos uma taxa de aproximadamente 15%.
- 54,7% da taxa de ocupação são de pessoas com ensino médio completo.
- menos de 1% é a taxa de ocupação de profissionais com mestrado e doutorado.
- Profissionais com superior completo, compreendem uma taxa de ocupação de 23,4%.

![](/image/ocupacao_idade_escolaridade.png)

---

## License

This project is licensed under the MIT License.
