"""
Desafio 19

Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
deles e escrevendo o nome do escolhido

"""

import random

print("{:=^35}".format(" Desafio 19 "))
nome_1 = input("Digite o 1° nome: ")
nome_2 = input("Digite o 2° nome: ")
nome_3 = input("Digite o 3° nome: ")
nome_4 = input("Digite o 4° nome: ")

nome_sorteado = random.choice([nome_1,nome_2,nome_3,nome_4])
print("O aluno sorteado para apagar o quadro foi {}".format(nome_sorteado))
print("{:=^35}".format(""))