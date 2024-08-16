# Receita total por vendedora
receita_por_vendedora = df.groupby('Vendedora')['Receita'].sum().sort_values(ascending=False)

# Visualizar
plt.figure(figsize=(10,6))
sns.barplot(x=receita_por_vendedora.index, y=receita_por_vendedora.values, palette='magma')
plt.title('Receita Total por Vendedora')
plt.xlabel('Vendedora')
plt.ylabel('Receita Total')
plt.xticks(rotation=45)
plt.show()
