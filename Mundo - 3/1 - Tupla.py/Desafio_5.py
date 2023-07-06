'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços
na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular.

from tabulate import tabulate
Produtos = (('Caneta..........R$', 2.00),
            ('Lapis...........R$', 2.50),
            ('Sabonete........R$', 12.50),
            ('Chinelo.........R$', 18.00),
            ('Porta retrato...R$', 16.50)) # Tupla aninhadas
print('{:-^25}\n{:>3}Listagem de produtos\n{:-^25}'.format('','',''))
colunas = ['Produtos', 'R$']
tabela = tabulate(Produtos, headers=colunas, floatfmt=".2f") # Formatação da tabela
print(tabela,'\n')
'''

Lista = ('Lapis', 2.00,
         'Caneta', 2.00,
         'Sabonete', 12.50,
         'Chinelo', 25.00,)
for n in range(0, len(Lista)):
    if n % 2 == 0:
        print(f'{Lista[n]:.<35}', end='')
    else:
        print(f'R$ {Lista[n]:>5.2f}')



