'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços
na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
Lista = ('Oculos', 36.00,
         'Caneta', 2.00,
         'Tinta guache', 10.00,
         'Sabonete liquido', 12.50)
for n in range(0,len(Lista)):
    if n % 2 == 0:
        print(f'{Lista[n]:.<30}',end='')
    else:
        print(f'R$ {Lista[n]:>5.2f}')