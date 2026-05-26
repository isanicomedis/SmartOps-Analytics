# =========================================================
# SMARTOPS ANALYTICS 
# limpeza_dados.py
# Script para limpeza e preparação dos dados 
# =========================================================


import pandas as pd 

df = pd.read_csv("dados/brutos/manutencao.csv")

print(df.columns)


print ("\nPrimeiras linhas dataset: ")
print(df.head())

print("\nInformações do dataset: ")
print(df.info())

df = df [
    [
        
        "Type", 
        "Air temperature [K]",
        "Process temperature [K]",
        "Torque [Nm]",
        "Rotational speed [rpm]",
        "Tool wear [min]",
        "Machine failure"
    ]
]

df = df.rename(    
    columns ={
        
        "Type": "machine_type",
        "Air temperature [K]": "air_temperature",
        "Process temperature [K]": "process_temperature", 
        "Torque [Nm]" : "torque",
        "Rotational speed [rpm]" : "rotational_speed",
        "Tool wear [min]" : "tool_wear",
        "Machine failure": "machine_failure"
    }
)

print("\nValores por coluna:")
print(df.isnull().sum())

df = df.dropna()

print("\nFormato final do dataset:")
print(df.shape)

df.to_csv(
    "dados/tratados/manutencao_tratada.csv",
    index=False
)

print("Dados tratados e salvos com sucesso!")

print("\nQuantidade de falhas:")
print(df["machine_failure"].value_counts())




# CSV bruto
# ↓
# Python lê os dados
# ↓
# Seleciona colunas importantes
# ↓
# Renomeia colunas
# ↓
# Verifica problemas# 
# ↓
# Remove valores vazios
# ↓
# Gera CSV tratado