'''
Aqui vão 10 exercícios práticos para você treinar análise de dados com essa planilha no Python (pandas e numpy):

🧮 Estatística e exploração de dados

    1 - Exiba as 5 primeiras e 5 últimas linhas do DataFrame. - ✅

    2 - Mostre o total de vendas (Valor Final) de todo o período. - ✅

    3 - Calcule a média, mediana e desvio-padrão dos valores finais. - ✅

    4 - Descubra qual produto teve a maior e a menor quantidade vendida. - ✅

    5 - Liste os 5 produtos mais vendidos (em quantidade total). - ✅

📆 Análise temporal

    6 - Agrupe as vendas por mês e calcule o total de “Valor Final” por mês.

    7 - Identifique o mês com o maior e o menor faturamento.

    8 - Crie um gráfico de linha mostrando a evolução do faturamento mensal.

🏬 Comparação entre lojas

    9 - Calcule o total de vendas por loja (ID Loja) e descubra qual mais vendeu.

    10 - Mostre o produto mais vendido em cada loja.
'''

# Importando bibliotecas
import pandas as pd
import numpy as np
from rich.jupyter import display

# Importando tabela e criando um DataFrame
vendas_lojas = pd.read_excel('vendas.xlsx')
table = pd.DataFrame(vendas_lojas)

# Visualizando as cinco primeiras e cinco últimas linhas do DataFrame
print(table.head(5))
print(table.tail(5))

# Visualizando o valor total de vendas
vendas_totais = table['Valor Final'].sum()
print(f"\nValor total de vendas de todas as filiais: R${vendas_totais}\n")

# Calculando a média, mediana e o desvio padrão
mean_vendas = table['Valor Final'].mean()
median_vendas = table['Valor Final'].median()
std_vendas = table['Valor Final'].std(ddof=0)

print(f"Média: {mean_vendas:.2f}\n")
print(f"Mediana: {median_vendas}\n")
print(f"Desvio Padrão: {std_vendas:.2f}\n")

# Calculando o produto mais vendido
more_sales = table.groupby('Produto')['Quantidade'].sum()
top_one = more_sales.idxmax()

print(f"Produto mais vendido: {top_one}")
print(f"Quantidade: {more_sales[top_one]}\n")

# Calculando os cinco mais vendidos
top_five = table.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).head(5)
print(f"Cinco produtos mais vendidos: {top_five}\n")

# Calculando as vendas por mês
table['ValorMes'] = table['Data'].dt.to_period('M')
vendas_mensais = table.groupby('ValorMes')['Valor Final'].sum()
print(f"Vendas mensais: {vendas_mensais}")