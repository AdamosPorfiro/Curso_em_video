'''
Crie um programa que vai gerar 5 numeros aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados 
e também indique o menor e o maior valor que estão da tupla
'''
from random import randint
lista = []
for c in range(5):
    n = randint(0, 999)
    lista.append(n)
Tupla = tuple(lista)
print(Tupla)
maior = 0
menor = Tupla[0]
for t in Tupla:
    if maior < t:
        maior = t
    if t < menor:
        menor = t
print(f'O maior número gerado é: {maior}\nO menor número gerado é: {menor}')
