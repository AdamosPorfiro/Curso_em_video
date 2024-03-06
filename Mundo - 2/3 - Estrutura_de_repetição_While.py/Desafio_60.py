"""
Faça um programa que leia um numero qualquer e mostre o seu fatorial.

Ex: 5! = 5x4x3x2x1= 120
"""
print("-="*20)
print("{:>25}".format(" Desafio 60 "))
print("-="*20)

n = int(input("Calcular seu fatorial: "))
cont = n
fatorial = 1
print(f"Calculando {n}! = ",end=' ')
while cont > 0:
    print(f"{cont} ", end=' ')
    print(f"x" if cont > 1 else "=", end=' ')
    fatorial *= cont
    cont -= 1
print(f" {fatorial}")
