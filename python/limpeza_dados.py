import pandas as pd 

# Lê o arquivo CSV com os dados brutos
df = pd.read_csv("dados/brutos/manutencao.csv")

# Exibe os nomes das colunas do dataset
print(df.columns)

# Mostra as primeiras linhas do dataset
print("\nPrimeiras linhas dataset: ")
print(df.head())

# Exibe informações gerais do dataset
print("\nInformações do dataset: ")
print(df.info())

# Seleciona apenas as colunas necessárias
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

# Renomeia as colunas para nomes mais simples
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

# Verifica valores nulos em cada coluna
print("\nValores por coluna:")
print(df.isnull().sum())

# Remove linhas com valores nulos
df = df.dropna()

# Exibe o formato final do dataset
print("\nFormato final do dataset:")
print(df.shape)

# Salva o dataset tratado em um novo arquivo CSV
df.to_csv(
    "dados/tratados/manutencao_tratada.csv",
    index=False
)

# Mensagem de sucesso
print("Dados tratados e salvos com sucesso!")

# Mostra a quantidade de falhas registradas
print("\nQuantidade de falhas:")
print(df["machine_failure"].value_counts())

