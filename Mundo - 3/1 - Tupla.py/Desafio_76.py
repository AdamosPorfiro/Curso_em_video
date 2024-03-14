'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços
na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular.

'''

produtos_com_valores = (
    'Caneta', 2.00, 'Lapis', 2.50, 'Apontador', 4.00, 'Borracha', 2.50, 'Tesoura', 5.00, 'Caderno', 28.00,
    'Mochila Escolar', 99.90, 'Cartolina', 2.00, 'Lapis de cor', 25.00, 'Caneta colorida', 8.50
)
<<<<<<< HEAD
palavra = ''
for pos, item in enumerate(produtos_com_valores[0::2]):
    print(f"{item:<20}......", end=' R$')
    print(" 2")
=======

for iten in range(0, len(produtos_com_valores),2):
    produtos_sem_valor = produtos_com_valores[iten]
    print(f"{produtos_sem_valor}")
    print("{:>20}".format("R$"))
        
>>>>>>> 97c9abf8f3899385538e01a9cffabb993237f1aa
