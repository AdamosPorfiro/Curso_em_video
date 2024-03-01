"""
Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artificios, 
indo de 10 até 0, com uma pausa de 1 segundo entre eles

"""

from time import sleep

for c in range(10,-1,-1): #Vai fazer a contagem tirando 1
    print(c)
    sleep(1)
print("-="*6)
print("BoOoOoOmMmM")
print("-="*6)


