"""
Desafio 28

Escreva um programa que faça o programa pensar em um numero inteiro entre 0 e 5 e peça para o usuario
tentar descobrir qual foi o numero escolhido pelo computador.

O programa deverá escrever na tela se o usuario perdeu ou venceu!
"""

from random import randint
from time import sleep

print("-="*30)
print("{:^60}".format("Vou pensar em um numero entre 0 e 5. TENTE ADIVINHAR..."))
print("-="*30)

n_aleatorio = (randint(0,5))
usuario = int(input("{:^17}Escolha o numero: ".format("")))
print("PROCESSANDO...")
sleep(2)

if n_aleatorio == usuario:
    print("\nPARABÉNS, você venceu!!!")
else:
    print("\nGANHEI, eu pensei no número {} e não no {}".format(n_aleatorio,usuario))
print("="*60)