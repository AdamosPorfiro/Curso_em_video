'''
Crie um programa que simule o funcionamento de um caixa eletronico.
No inicio, pergunte ao usuario qual será o valor a ser sacado (numero inteiro)
e o programa vai dizer quantas cedulas de cada valor serão entregues.

OBS: Considere que  o caixa possui cedulas de:
R$50 R$20 R$10 e R$1

Vamos desenvolver um loop infinito que irá repetir todo o bloco;
'''
Cedulas_50 = 50
Cedulas_20 = 20
Cedulas_10 = 10
Cedulas_1 = 1
while True:
    n = str(input('Qual valor a ser sacado R$ '))
    if n.isdigit():
        break
    else:
        continue # Funciona
'''
Dizer para o usuario quantas cedulas de cada valor serão entregues;
'''
n=int(n)
for c in range(1,50):
    




