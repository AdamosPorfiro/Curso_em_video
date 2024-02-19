"""
Desafio 30

Crie um programa que leia um numero inteiro qualquer e diga se ele é PAR ou IMPAR
"""

print("{:=^25}".format(" Desafio 30 "))
n = int(input("Digite um número: "))
if n % 2 == 0:
    print("\nO número {} é par".format(n))
else:
    print("\nO número {} é ímpar".format(n))
print("{:=^25}".format(""))