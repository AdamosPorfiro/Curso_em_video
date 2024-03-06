"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n
primeiros elementos de uma SEQUÊNCIA DE FIBONACCI.

Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8

A sequência subsequente corresponde a soma dos dois numero anteriores:
Ex.: Termo = 8

T = antecessor + termo
T = 7+8
T = 15

Assim, temos a sequência:

 8 > 15 > 29 > 57 > 113...n
"""
print("-="*20)
print("{:>25}".format(" Desafio 63 "))
print("-="*20)
n = int(input("Quantos termos você quer ver: "))
t1 = 0
t2 = 1
print("-="*30)
print(f"{t1} ⮕ {t2}",end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f"⮕ {t3}", end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print("Fim")
