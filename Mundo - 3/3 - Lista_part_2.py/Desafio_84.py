'''
Faça um programa que leia o nome e peso de varias pessoas e guarde tudo em uma lista. No final mostre

a - Quantas pessoas foram cadastradas

b - Uma listagem com as pessoas mais pesadas

c - Uma listagem com as pessoas mais leve
'''
#Lista com os nomes
nomes_pesos = []
copia_nomes_pesos = []

#Maior peso
pessoas_maior_pesos = []
copia_maior_peso = []
#Menor peso
pessoas_menor_pesos = []
copia_menor_peso = []

#Quantidade de pessoas cadastradas
qtd_pessoas_cadastradas = 0

#Armazena informação em uma lista e em seguida faz uma copia criando uma lista dentro de outra lista
while True:
    print("-="*15)
    nomes_pesos.append(str(input("Digite o seu nome: ")))
    nomes_pesos.append(float(input("Digite o seu peso: ")))
    qtd_pessoas_cadastradas += 1
    copia_nomes_pesos.append(nomes_pesos[:])
    nomes_pesos.clear()
    print("-="*15)

    #Verificação de continuação
    while True:
        continuar = str(input("Deseja continuar [S|N]: ")).upper().strip()
        if continuar not in 'SN':
            continue
        elif continuar in 'SN':
            break
    if continuar in 'N':
        break
#========================================================================================
#Faz a leitura dos dados, separa cada 1 na lista correspondente e copia para outra lista criando novamente
#Uma lista dentro da lista e faz a limpeza das anteriores
for c in copia_nomes_pesos:
    if c[1] >= 90:
        pessoas_maior_pesos.append(c[0])
        pessoas_maior_pesos.append(c[1])
        copia_maior_peso.append(pessoas_maior_pesos[:])
        pessoas_maior_pesos.clear()
    elif c[1] < 90:
        pessoas_menor_pesos.append(c[0])
        pessoas_menor_pesos.append(c[1])
        copia_menor_peso.append(c[:])
        pessoas_menor_pesos.clear()
#=========================================================================================
#Exibi quantidade e utiliza for para imprimir as pessoas mais pesadas e mais leves
print("~"*30)
print(f"{qtd_pessoas_cadastradas} foram cadastradas")
print("-"*30)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print(f"\33[1;34mPessos com peso acima de 90kg\33[m")
print("-"*30)
for c in copia_maior_peso:
    print(f"{c[0]} com {c[1]}kg")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print("-="*15)
print("-"*30)
print(f"\33[1;34mPessoa com peso abaixo de 90kg\33[m")
print("-"*30)
for c in copia_menor_peso:
    print(f"{c[0]} com {c[1]}kg")
print("~"*30)
