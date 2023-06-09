'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
 Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
resultado = 0
n3 = 0
while n3 != 5:
    n1 = float(input('{:=^38}\nInforme o primeiro numero: '.format(''))) 
    n2 = float(input('Informe o segundo numero: '))
    n3 = int(input('''
    [1] Somar
    [2] Multiplicar   
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    Escolha: '''))
    if n3 != 1 and n3!=2 and n3!=3 and n3!=4 and n3!=5:
        print ('Informção incorreta, tente novamente')
    if n3 == 1:
        resultado = n1+n2
        print('\nA soma dos números {} + {} = {}'.format(n1,n2,resultado))
    elif n3 == 2:
        resultado = n1*n2
        print('\nA multiplicação dos números {} x {} = {}'.format(n1,n2,resultado))
    elif n3 == 3:
        if n1 > n2:
            print('\nO maior número digitado foi: {}'.format(n1))
        elif n2 > n1:
            print('\nO maior número digitado foi: {}'.format(n2))
        else:
            print('\nAmbos valores digitados são iguais')
    elif n3 == 4:
        print('\nReiniciando...')
        sleep(1)
    elif n3 == 5:
        print('\nSaindo...')
        sleep(1)
print('Obrigado!')


