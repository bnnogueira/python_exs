# Importando os pacotes que iremos usar para a análise
import pandas as pd
import plotly.express as px

# Importando a tabela que será utilizada na análise
tabela = pd.read_csv('ClientesBanco.csv', encoding='latin1')

# Removendo uma coluna que não será útil para a análise
tabela = tabela.drop("CLIENTNUM", axis=1)

# Visualizando a primeiras linhas da tabela
print(tabela.head())

# Visualizando as últimas linhas da tabela
print(tabela.tail())

# Removendo as linhas da tabela que tem campos vazios
tabela = tabela.dropna()

# Mostrando as informações da tabela
print(tabela.info())

# Descrevendo os dados da tabela e arredondando as casas decimais
print(tabela.describe().round(1))

# Mostrando a quantidade de clientes em atividade e o total de cancelamentos
quantidade_categoria = tabela["Categoria"].value_counts()

# Mostrando os mesmos dados, porém em percentual
qtd_percentual = tabela["Categoria"].value_counts(normalize=True)

print(quantidade_categoria)
print(qtd_percentual)

for coluna in tabela:
  grafico = px.histogram(tabela, x=coluna, color="Categoria")
  grafico.show()

"""# Informações retiradas da análise:
  - Quanto mais produtos contratados um cliente tem, menor é a chance dele cancelar.
  - Quanto mais transações realizadas, menor a chance do cliente cancelar.
  - Quanto maior a quantidade de contatos do cliente, maior a chance dele cancelar o plano (o contato possivelmente pode ser um problema).
"""