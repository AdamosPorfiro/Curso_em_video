'''
Crie um programa que vai gerar 5 numeros aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados 
e também indique o menor e o maior valor que estão da tupla
'''
from random import randint
Lista = []
for c in range(5):
    n = randint(0, 999)
    Lista.append(n)
Tupla = tuple(Lista)
print(Tupla)
maior = 0
menor = Tupla[0]
for m in Tupla:
    if maior < m:
        maior = m
    if m < menor:
        menor = m
print(f'Maior numero é: {maior}\nO menor número é: {menor}')
print('='*30)
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os números sorteados são: {numeros}')
print(f'O maior numero é: {max(numeros)}\nO menor numero é: {min(numeros)}')
