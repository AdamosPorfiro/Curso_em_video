'''
Faça um programa que leia o nome e peso de varias pessoas e guarde tudo em uma lista. No final mostre

a - Quantas pessoas foram cadastradas

b - Uma listagem com as pessoas mais pesadas

c - Uma listagem com as pessoas mais leve
'''

nomes_pesos = []
copia_nomes_pesos = []
qtd_pessoas_cadastradas = 0
while True:
    print("-="*15)
    nomes_pesos.append(str(input("Digite o seu nome: ")))
    nomes_pesos.append(float(input("Digite o seu peso: ")))
    qtd_pessoas_cadastradas += 1
    copia_nomes_pesos.append(nomes_pesos[:])
    nomes_pesos.clear()
    print("-="*15)
    while True:
        continuar = str(input("Deseja continuar [S|N]: ")).upper().strip()
        if continuar not in 'SN':
            continue
        elif continuar in 'SN':
            break
    if continuar in 'N':
        break
print(f"{qtd_pessoas_cadastradas} foram cadastradas")

