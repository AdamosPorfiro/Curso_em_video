"""
Faça um programa que leia um numero qualquer e mostre o seu fatorial.

Ex: 5! = 5x4x3x2x1= 120
"""
print("-="*20)
print("{:>25}".format(" Desafio 60 "))
print("-="*20)

n = int(input("Informe o numero para receber o fatorial: ")) + 1
fatorial = 1
while n != 1:
    fatorial = (n-1)*fatorial
    n -= 1
    if n > 0:
        print(f"{n} ", end=' ⮕ ')
print(f" {fatorial}")
