"""
Desafio 16

Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira;

Ex: Digite um numero: 6.127 o numero 6.127 tem a parte inteira 6.

"""
from math import trunc
num = float(input("Digite um numero real: ")) 
print("A parte inteira do numero {} é {}".format(num, trunc(num))) # Vai truncar o numero e mostrar apenas o numero inteiro