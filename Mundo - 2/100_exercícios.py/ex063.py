'''
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
'''
print('{:=^40}\n{:^8}SEQUÊNCIA DE FIBONACCI\n{:=^40}\n'.format('','',''))
n1 = float(input('{:^6}Quantos termos deseja ver? '.format('')))
'''for c in range(1,6):
    n1 = n1-1+n1
    print('> {} '.format(n1), end='')'''
Repetidor = 0
t1 = 0
t2 = 1
print ('> {} > {} > '.format(t1,t2),end='')
while Repetidor < n1:
    t3 = t1 + t2
    Repetidor += 1
    print(' {} >'.format(t3),'FIM' if Repetidor == n1 else '', end='')
    t1 = t2
    t2 = t3
print('\n{:=^40}'.format(''))




