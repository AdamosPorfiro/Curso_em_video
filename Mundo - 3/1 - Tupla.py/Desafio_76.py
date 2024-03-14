'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços
na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular.

'''

produtos_com_valores = (
    'Caneta', 2.00, 'Lapis', 2.50, 'Apontador', 4.00, 'Borracha', 2.50, 'Tesoura', 5.00, 'Caderno', 28.00,
    'Mochila Escolar', 99.90, 'Cartolina', 2.00, 'Lapis de cor', 25.00, 'Caneta colorida', 8.50
)

print("Listagem de Preços:")
print("=" * 30)
print("{:<20} {:>10}".format("Produto", "Preço"))
print("-" * 30)

for i in range(0, len(produtos_com_valores), 2):
    produto = produtos_com_valores[i]
    preco = produtos_com_valores[i + 1]
    print("{:<20} R$ {:>8.2f}".format(produto, preco))

        