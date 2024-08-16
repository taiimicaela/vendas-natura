import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o CSV com os dados das vendas
df = pd.read_csv('vendas_natura.csv')

# Ver as primeiras linhas do dataframe
print(df.head())

# Converter a coluna de data para datetime
df['Data'] = pd.to_datetime(df['Data'])

# Adicionar uma coluna de receita total (Quantidade * Preço Unitário)
df['Receita'] = df['Quantidade'] * df['Preço Unitário']

# Resumo estatístico
print(df.describe())
