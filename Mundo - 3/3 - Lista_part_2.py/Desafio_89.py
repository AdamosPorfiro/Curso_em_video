'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individual.

lista_1 = []
lista_composta = []

while True:
    dados_1 = nome
    append(dados_1)
    nota_1 = float
    append(nota_1)
    nota_2 = float
    append(nota_2)
    lista_composta.append(lista_1[:])
'''

lista_nomes_notas = []
lista_composta = []

while True:
    lista_nomes_notas.append(input("Nome: "))
    lista_nomes_notas.append(input("1° nota: "))
    lista_nomes_notas.append(input("2° nota: "))
    lista_composta.append(lista_nomes_notas[:])
    lista_nomes_notas.clear()
    while True:
        continuar = str(input("Deseja continuar [S|N]: ")).strip().upper()
        if continuar not in 'SN':
            continue
        elif continuar in 'S':
            break
        elif continuar in 'N':
            break
    if continuar in 'N':
        break
#Calculando a média------------------------------------------------------------------
for p,n in enumerate(lista_composta):
    print(f"{n[1]}")
    print(f"{n[2]}")
print("-"*20)
print(f"{'Boletim':>13}")
print("-"*20)

