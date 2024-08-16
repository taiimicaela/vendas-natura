# Receita total por data
receita_por_data = df.groupby('Data')['Receita'].sum()

# Visualizar
plt.figure(figsize=(10,6))
plt.plot(receita_por_data.index, receita_por_data.values, marker='o')
plt.title('Receita Total ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Receita Total')
plt.grid(True)
plt.show()
