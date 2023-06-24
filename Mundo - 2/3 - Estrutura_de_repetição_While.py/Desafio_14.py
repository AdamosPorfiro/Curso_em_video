'''
Crie um programa que leia o nome e o preço de varios produtos.
O programa deverá perguntar se o usuario vai continuar.
No final, mostrar:

A - Qual é o total gasto na compra
B - Quantos produtos custam mais que R$ 1000
C - Qual é o nome do produto mais barato

'''
Total_gasto  = Qtd_1000  = 0
Preco_barato = float('inf')
Produto_mais_barato  = ''
while True:
    while True:
        Produto = str(input('Produto: '))
        Preco = float(input('Preço R$ '))
        Total_gasto+=Preco
        if Preco > 1000:
            Qtd_1000 += 1
        if Preco<Preco_barato:
            Preco_barato = Preco
            Produto_mais_barato = Produto
        while True:
            Sair_continuar = str(input('Continuar [S/N]: ')).upper().strip()[0]
            if Sair_continuar not in 'SN':
                continue
            elif Sair_continuar in 'S':
                break
            elif Sair_continuar in 'N':
                break
        if Sair_continuar in 'N':
            break
    break
print(f'\nTotal gasto R$ {Total_gasto:,}\nQuantos produtos custaram mais de R$ 1000: {Qtd_1000} un\nProduto mais barato: {Produto_mais_barato}' )