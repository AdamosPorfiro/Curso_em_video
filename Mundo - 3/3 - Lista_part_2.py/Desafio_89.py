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

nome = str(input("Nome: "))
nota_1 = float(input("1° Nota: "))
nota_2 = float(input("2° Nota: "))
media = 2*(nota_1+nota_2)
ficha.append((nome,(nota_1, nota_2), media))

print(ficha)