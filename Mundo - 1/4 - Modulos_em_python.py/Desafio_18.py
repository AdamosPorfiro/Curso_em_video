"""
Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

"""
from math import sin,cos,tan, radians
from time import sleep

print("{:=^40}".format(" Desafio 18 "))
ang = float(input("Digite um angulo: "))

seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print("Calculando Angulo SENO, COSSENO e TANGENTE...")
sleep(2.5)
print("\nSeno {:.2f}\nCosseno {:.2f}\nTangente {:.2f}".format(seno, coss, tang))
print("{:=^40}".format(""))