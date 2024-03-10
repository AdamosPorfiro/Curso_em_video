'''
Crie um programa que leia o nome e o preço de varios produtos.
O programa deverá perguntar se o usuario vai continuar.
No final, mostrar:

A - Qual é o total gasto na compra
B - Quantos produtos custam mais que R$ 1000
C - Qual é o nome do produto mais barato

'''
total_gasto = mais_de_mil  = 0
produto_mais_barato = ' '
primeiro_produto = True

while True:
    print("="*30)
    nome_prod = str(input("Nome do produto: "))
    preço_prod = float(input("Preço do produto: "))
    print("="*30)
    total_gasto += preço_prod
    if preço_prod > 1000:
        mais_de_mil += 1

    #Produto mais barato
    if primeiro_produto or preço_prod < preço_prod_mais_barato:
        preço_prod_mais_barato = preço_prod
        produto_mais_barato = nome_prod
        primeiro_produto = False
    
    #Continuar ou sair
    while True:
        cont = str(input("Quer continuar [S | N]: ")).strip().upper()
        if cont in 'S':
            break
        elif cont in 'N':
            break
    if cont in 'N':
        break
print("-"*50)
print(f"Total gasto R$ {total_gasto}")
print(f"{mais_de_mil} produtos custaram mais de R$ 1000")
print(f"O nome do produto mais barato é {produto_mais_barato} custando R$ {preço_prod_mais_barato:2}")