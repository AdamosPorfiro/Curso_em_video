"""
Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.

"""

n = int(input("Informe um numero inteiro: "))

divisor = 0

for c in range(1, n+1):
    if n % c == 0: # Se o numero informado for divisivel por 3 numeros ele não é primo
        divisor += 1
if divisor >= 3:
    print("Esse número não é primo")
else:
    print(f"Sim, {n} é um número primo")
    