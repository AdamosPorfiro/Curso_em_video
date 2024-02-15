"""
Desafio 20
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

import random

nome_1 = input("Nome do 1° aluno: ")
nome_2 = input("Nome do 2° aluno: ")
nome_3 = input("Nome do 3° aluno: ")
nome_4 = input("Nome do 4° aluno: ")

ord_sort = random.sample([nome_1,nome_2,nome_3,nome_4], k=4)

print("A orden de apresentção é {}".format(ord_sort))