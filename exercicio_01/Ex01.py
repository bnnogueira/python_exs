'''
Exercícios Pandas e NumPy

🧠 Parte 1 — NumPy

1 - Crie um array com as vendas de todas as filiais e calcule:

    ✅ Média das vendas
    ✅ Valor máximo e mínimo
    ✅ Desvio padrão

2 - Gere um array 3x3 com números aleatórios e:

    ✅ Calcule a soma de cada linha e coluna
    ✅ Normalize o array (valores entre 0 e 1)

3 - ✅ Crie dois arrays de mesmo tamanho representando vendas e custos, e calcule o lucro total (vendas - custos).

4 - ✅ Gere um array de 12 valores representando a receita mensal, e use np.argmax() e np.argmin() para identificar o mês de maior e menor receita.
'''

#Parte 1

# Importando bibliotecas
import pandas as pd
import numpy as np

# Lendo arquivo CSV
vendas = pd.read_csv('vendas_mensais.csv')

# Calculando a média de todas as filiais
media = vendas['Vendas'].mean()
print(f"Média de vendas mensais de todas as filiais: ${media}\n")

#Calculando e venda mínima e venda máxima
venda_minima = vendas['Vendas'].min()
venda_maxima = vendas['Vendas'].max()

print(f"O valor da venda mínima foi de: ${venda_minima}.\nEnquanto o da venda máxima foi de: ${venda_maxima}.\n")

# Calculando o desvio padrão e a média

dados = pd.DataFrame(vendas)
desvio = dados['Vendas'].std(ddof=0)

print(f"\nMédia das vendas: ${media:.2f}")
print(f"Desvio padrão das vendas: {desvio:.2f}")


# Parte 2

# Gerando um array 3x3
print("\nGerando um array com números aleatórios entre 1 e 10.\n")
array_gerado = np.random.randint(1, 10, (3,3))
print(f"Linhas geradas:\n{array_gerado}")

# Calculando a soma das linhas
soma_linhas = np.sum(array_gerado, axis = 1)
print(f"\nSoma das linhas: {soma_linhas}")

# Calculando a soma das colunas
soma_colunas = np.sum(array_gerado, axis = 0)
print(f"\nSoma das colunas: {soma_colunas}")

# Normalizando o array
min_val = np.min(array_gerado)
max_val = np.max(array_gerado)

array_normal = (array_gerado - min_val) / (max_val - min_val)

print(f"\nArray original:\n\n{array_gerado}")
print(f"\nArray normalizado:\n\n{array_normal}\n\n")

# Parte 3

# Criando uma nova coluna e calculando o lucro total
vendas['Lucro Total'] = vendas['Vendas'] - vendas['Custo']
lucro_total = vendas['Lucro Total'].sum()
print(f"O lucro total foi de: ${lucro_total}")

# Parte 4

# Gerar um array de 12 valores aleatórios representando a receita mensal
receitas_mensais = np.random.randint(2000, 15000, size=12)

# Identificar o mês de maior receita
mes_maior_receita = np.argmax(receitas_mensais)

# Identificar o mês de menor receita
mes_menor_receita = np.argmin(receitas_mensais)

# Exibir resultados
print(f"\nReceitas mensais: {receitas_mensais}")
print(f"\nMês com maior receita: {mes_maior_receita + 1}")  # +1 para representar o mês (1 a 12)
print(f"Mês com menor receita: {mes_menor_receita + 1}")  # +1 para representar o mês (1 a 12)
