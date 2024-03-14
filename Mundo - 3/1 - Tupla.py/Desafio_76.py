'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços
na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular.

'''

produtos_com_valores = (
    'Caneta', 2.00, 'Lapis', 2.50, 'Apontador', 4.00, 'Borracha', 2.50, 'Tesoura', 5.00, 'Caderno', 28.00,
    'Mochila Escolar', 99.90, 'Cartolina', 2.00, 'Lapis de cor', 25.00, 'Caneta colorida', 8.50
)
print("="*40)
print("="*40)
print("Produtos {:>30}".format(" Preços "))
print("-"*40)
#Função zip() combina os produtos com seus respectivos preços e então imprimi cada par formatado adequadamente
for produtos, preços in zip(produtos_com_valores[0::2], produtos_com_valores[1::2]):
    print("{:<15}..................R$ {:4}".format(produtos, preços))
