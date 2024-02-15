"""
Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

"""
from math import sin,cos,tan, radians

print("{:=^40}".format(" Desafio 18 "))
ang = float(input("Digite um angulo: "))

seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print("\nSeno {}\nCosseno {}\nTangente {}".format(seno, coss, tang))
print("{:=^40}".format(""))