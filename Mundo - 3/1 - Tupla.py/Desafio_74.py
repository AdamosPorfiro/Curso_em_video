'''
Crie um programa que vai gerar 5 numeros aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados 
e também indique o menor e o maior valor que estão da tupla
'''

from random import sample #Sample gera números aleatorios de uma sequencia definida("")

print("-="*20)
print("{:>25}".format(" Desafio 74 "))
print("-="*20)

valores_gerados = () #Tupla vazia
maior  = 0


numeros_aleatorios = sample(range(101),5) #Range é a quantidade, faixa de números que ele tera disponivel
valores_gerados = numeros_aleatorios
menor = valores_gerados[0]

print(valores_gerados)

for pos,numero in enumerate(valores_gerados):
    
    # Maior
    if numero > maior:
        maior = numero
    
    #Menor
    if numero < menor:
        menor = numero
print(f"Maior {maior}\nMenor {menor}")

