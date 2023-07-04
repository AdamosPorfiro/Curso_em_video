'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços
na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
from tabulate import tabulate
Produtos = [('Caneta............', 2.00),
            ('Lapis.............', 2.50),
            ('Sabonete liquido..', 12.50),
            ('Chinelo...........', 18.00),
            ('Porta retrato.....', 16.50)]

colunas = ['Produtos', 'R$']
tabela = tabulate(Produtos, headers=colunas, floatfmt=".2f")
print(tabela)

