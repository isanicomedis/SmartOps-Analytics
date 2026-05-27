# Importando as bibliotecas
# pandas - análise de dados
import pandas as pd
# matplotlib - criação de gráficos
import matplotlib.pyplot as plt

# le o dataset tratado
df = pd.read_csv("dados/tratados/manutencao_tratada.csv")


# mostrando as primeiras linhas
print("\nPrimeiras linhas do dataset:")
print(df.head())

# quantidade total de maquinas
total_maquinas = len(df)

print("\nTotal de máquinas:")
print(total_maquinas)

# quantidade de falhas
total_falhas = df["machine_failure"].sum()

print("\nQuantidade de falhas:")
print(total_falhas)

# media de torque
media_torque = df["torque"].mean()

print("\nMédia de torque:")
print(round(media_torque, 2))


# MÉDIA DA TEMPERATURA DO PROCESSO
media_temperatura = df["process_temperature"].mean()

print("\nMédia da temperatura do processo:")
print(round(media_temperatura, 2))

# QUANTIDADE DE MÁQUINAS POR TIPO
print("\nQuantidade de máquinas por tipo:")

print(df["machine_type"].value_counts())

# GRÁFICO DE FALHAS

# contando valores de falha
falhas = df["machine_failure"].value_counts()

# criando gráfico
falhas.plot(kind="bar")

# título do gráfico
plt.title("Quantidade de Falhas")

# nome eixo x
plt.xlabel("Falha")

# nome eixo y
plt.ylabel("Quantidade")

# mostrando gráfico
plt.show()


# GRÁFICO DE TIPOS DE MÁQUINAS
tipos = df["machine_type"].value_counts()

tipos.plot(kind="bar")

plt.title("Tipos de Máquinas")

plt.xlabel("Tipo")

plt.ylabel("Quantidade")

plt.show()