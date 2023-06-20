'''
Crie um programa que leia o nome e o preço de varios produtos.
O programa deverá perguntar se o usuario vai continuar.
No final, mostrar:

A - Qual é o total gasto na compra
B - Quantos produtos custam mais que R$ 1000
C - Qual é o nome do produto mais barato

'''
Total_gasto = 0
while True:
    while True:
        Produto = str(input('Produto: '))
        Preço = str(input('Preço R$ '))
        while True:
            Sair_continuar = str(input('Continuar [S/N]: ')).upper().strip()[0]
            if Sair_continuar not in 'SN':
                continue
            elif Sair_continuar in 'N':
                break
            elif Sair_continuar in 'S':
                break
        if Sair_continuar in 'S':
            print(f'\nQual é o total gasto R$ {}\nProdutos custam mais de R$ 1000: {}\nNome do produto mais caro: {}')
            break
    break