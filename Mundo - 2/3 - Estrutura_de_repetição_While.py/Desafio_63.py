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

n = int(input("Informe um número: "))
qtd_termos = 0

termo_atual = n
proximo_termo = n-1

while qtd_termos != 7:
    print(f"{termo_atual}",end=' ⮕ ')

    termo_seguinte = termo_atual + proximo_termo # 9
    termo_atual = termo_seguinte
    termo_seguinte = proximo_termo
    
    qtd_termos += 1
print("Acabou")