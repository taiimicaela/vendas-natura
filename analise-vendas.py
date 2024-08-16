# Receita total por produto
receita_por_produto = df.groupby('Produto')['Receita'].sum().sort_values(ascending=False)

# Visualizar
plt.figure(figsize=(10,6))
sns.barplot(x=receita_por_produto.index, y=receita_por_produto.values, palette='viridis')
plt.title('Receita Total por Produto')
plt.xlabel('Produto')
plt.ylabel('Receita Total')
plt.xticks(rotation=90)
plt.show()
