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

Os dados da Rais são geralmente bem grandes, geralmente algo aproximadamente de 10GB ou mais. Nesse projeto esses arquivos são acessados diretamente do servidor [FTP](ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2024/) do Ministério do Trabalho, através de uma aplicação de ETL que está contida no módulo [`data_processing`](/scripts/data_processing.py).

**Limpeza e pré-processamento**:

Foi realizada a filtragem apenas das variáveis de interesse, assim como também o município alvo, que no caso é a cidade de São Paulo. As observações das variáveis da base de dados da Rais são codificadas, então foi necessário traduzir essas informações com base nos [`metadados oficiais`](/dados/dicionario_rais.xls). O dicionário com os valores utilizados na tradução está contido no módulo [`data_processing`](/scripts/data_processing.py), que também contém outras funcionalidades utilizadas na extração e pré-processamento dos dados.

Após filtragem e tradução dos dados, o dataset contém 11 variáveis — 6 são as variáveis originais codificadas e 5 são as variáveis com as observações traduzidas — e 6.669.537 observações. Não possui dados faltantes e os outliers encontrados tratam de informações válidas e que por tanto não foram removidos. 

Todas as variáveis de interesse após tradução são do tipo qualitativas, nominais e ordinais. Foi necessário realizar a trasformação das variáveis categóricas ordinais para que fossem preservadas as ideias de ordem destes dados.

Foram criados datasets menores com informações específicas para facilitar em algumas técnincas de visualização, como foi o caso do gráfico de barras que obtém a taxa de ocupação por gênero (dataset `taxa_ocupacao_genero`). Outra técnica de visualização onde foi criado outro dataset com informações específicas foi o `distribution_sex` que é utilizado para visualizar a distribuição salarial no contexto de gênero.

**Análise exploratória**:

- Estatística Descritiva: 

Todas as técnicas de estatística descritivas utilizadas são estratégias específicas quando tratamos de dados categóricos, uma vez que não são dados que podemos quantificar com medidas de tendência central como média e de disperção como variância e desvio padrão. No entanto, ainda conseguimos utilizar a moda, através das frequências de distribuições com gráficos de barras, ou mediana e intervalo interquartil, nos casos de dados ordinais através dos bloxplots e violinos por exemplo. Algumas das técnicas utlizadas foram:

- Gráficos de barras para avaliar a distribuição de frequência salarial no contexto de gênero, assim como as taxas de ocupação por faixa  etária, escolaridade e gênero.
- Boxplot para avaliar a variabilidade salarial com intervalo interquartil e a porcentagem de trabalhadores com relação a faixa média salarial através dos quartis.
- Violino para visualizar não apenas a variabilidade salarial entre os grupos étnicos, mas também as desnidades de cada grupo conforme as faixas salariais.

---

## Insights e Conclusão

Avaliado a distribuição de acordo com cada faixa salarial na cidade de São Paulo, observamos uma distribuição assimétrica positiva, onde os maiores salários se concentram em poucos indivíduos. 28% dos indivíduos estão na faixa de 1,01 a 1,5 salários mínimos (moda), e 2,2% estão na faixa salarial de até 0,5 salários mínimos, enquanto que indivíduos que recebem a partir de 4 salários mínimos são menos que 5%.

![](/image/distribuicao_faixas_salariais.png)

Agora, avaliando a distribuição salarial com o boxplot, observamos que 25% dos trabalhadores estão abaixo da faixa média salarial de 1, 01 a 1,50 salários mínimos, enquanto 50% dos trabalhadores estão entre as faixas médias salariais de 1,01 a 1,50 salários mínimos e 3,01 a 4,00 salários mínimos. Apenas 25% dos trabalhadores estão acima das faixas médias salarias de 3,01 a 4,00 salários mínimos. Os pontinhos que são tidos como outliers, na verdade apenas demonstram que há indivíduos que chegam a faixas médias salariais maiores que 10,01 a 15,00 salários mínimos.

![](/image/boxplot_faixas_salariais.png)

Considerando a distribuição salarial em um contexto de gênero, percebemos que as mulheres são maioria quando os salários são mais baixos, já os homens predominam os salários mais altos, conforme conseguimos observar nas primeiras 3 faixas médias salariais. A taxa de ocupação dos homens também é maior em relação as mulheres, 52,7% para homens e 47,3% para mulheres.

![](/image/ocupacao_distribuicao_combined.png) 

Já com relação a etnia, vemos que os grupos pardos, pretos e indígenas possuem 50% dos indivíduos entre as faixas médias salariais de 1,01 a 1,50 salários mínimos e 2,01 a 3,00 salários mínimos, equanto brancos possuem 50% dos seus representantes entre as faixas médias salariais de 1,01 a 1,50 salários mínimos e 4,01 a 5,00 salários mínimos. Já para o grupos da etnia amarela, os indivíduos estão entre as faixas médias salariais de 1,01 a 1,50 a 5,01 a 7,00 salários mínimos. Isso denota uma maior desigualdade para os grupos pardos, pretos e indígenas, eles possuem uma menor variabilidade salarial em comparação aos brancos e amarelos. Olhando para os grupos pardos, pretos e indígenas, 75% dos seus representantes estão abaixo das faixas médias salariais de 2,01 a 3,00 salários mínimos, apenas 25% entre acimas destas faixas médias salariais. Já o grupo dos brancos possui 75% de sua população abaixo da faixa média salarial de 4,01 a 5,00 salários mínimos, com 25% acima destas faixas médias salariais. Amerelos possuem 75% dos seus indivíduos abaixo das faixas médias salariais de 5,01 a 7,00, com 25% acima destas faixas médias salariais. Observando a densidade entre os grupos, os indígenas possuem uma maior densidade nas menores faixas médias salariais, o que sugere uma maior desiqualdade neste grupo.

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
