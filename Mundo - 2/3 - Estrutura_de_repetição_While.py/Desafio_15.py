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

Teria uma forma de fazer um contador onde ele conte o valor que o usuario digitou e 
através das condições ele mostre para o usuario as cedulas que ele irá receber;
'''
n=int(n)
if n >= 1 and n <= 5:
    for c in range(1,n+1):
        n=c
    print(f'Você receberá {n} cedulas de R$ {Cedulas_1}')

    




