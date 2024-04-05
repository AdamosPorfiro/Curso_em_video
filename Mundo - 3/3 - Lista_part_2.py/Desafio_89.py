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

ficha = list()

while True:
    nome = str(input("Nome: "))
    nota_1 = float(input("1° Nota: "))
    nota_2 = float(input("2° Nota: "))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome,[nota_1, nota_2], media])
    resp = str(input("Quer continuar [S|N]: ")).upper().strip()
    if resp == "N":
        break
print("-="*20)
print(f"{"No.":<8}{"NOME":12}{"NOTA":>2}")

for p, a in enumerate(ficha):
    print(f"{p+1:<8}{a[0]:<12}{a[2]:>2.1f}")

while True:
    print("-"*35)
    opc = int(input("Mostrar notas de algum aluno? [999 - para sair]: "))
    if opc == 999:
        print("FINALIZANDO...")
        break
    elif opc <= len(ficha):
        print(f"Notas de {ficha[opc-1][0]} são {ficha[opc-1][1]}")
print("<<<< VOLTE SEMPRE >>>>")
