"""
Desafio 28

Escreva um programa que faça o programa pensar em um numero inteiro entre 0 e 5 e peça para o usuario
tentar descobrir qual foi o numero escolhido pelo computador.

O programa deverá escrever na tela se o usuario perdeu ou venceu!
"""

from random import randint
print("{:=^40}".format(" Desafio 28 "))
n_aleatorio = (randint(0,5))
print("Descubra o numero gerado pelo computador")
usuario = int(input("Informe o número de 0 á 5: "))
if usuario == n_aleatorio:
    print("\nPARABÉNS, você venceu!!!")
else:
    print("\nVocê perdeu, tente novamente!")
print("{:=^40}".format(""))