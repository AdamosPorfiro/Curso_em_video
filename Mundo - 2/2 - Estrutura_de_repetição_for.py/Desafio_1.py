'''
Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artificios, indo de 10 até 0,
com uma pausa de 1 segundo entre eles

Analise: 
For = Para fazer a contagem de 10 até 0;
modulo TIME a função SLEEP para fazer uma pausa de 1 seg;

'''
print('\n'+'{:^10}'.format('Contador regressiva'))
from time import sleep
for c in range(10,0,-1):
    print(c)
    sleep(1)