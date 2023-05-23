'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

1 - Quais são os dados de entrada?
- input n1,n2,n3

2 - O que devo fazer com esses dados?
- Exibir qual é o maior e qual é o menor

3 - Qual é a restrição desse problema?
- São apenas 3 numeros;
- Apenas 2 serão exibidos na tela

4 - Qual é o resultado esperado?
- Exiba na tela qual é o maior numero e qual é o menor numero.

5 - Quais são os passos para se alcançar o resultado?
#1 input n1, n2, n3
#2 if n1 > n2 e n1 > n3
    print n1 é maior
        if n2 < n3
            print n2 é menor
        else
            print n3 é menor
    if n2 > n1 e n2 > n3
        print n2 é maior
        if n1 < n3
            print n1 é menor
        else
            print n3 é menor
    if n3 > n1 e n3 > n2
        print n3 é maior
            if n2 < n1
                print n2 é menor
            else 
                print n1 é menor
'''
print('\n' + '=' * 20, 'Qual numero é o maior', '=' * 20)
n1 = float(input('\nInforme o primeiro número:\nNúmero 1: '))
n2 = float(input('Informe o segundo número:\nNúmero 2: '))
n3 = float(input('Informe o terceiro número:\nNúmero 3: '))
if n1 > n2 and n1 > n3:
    print ('{} é o maior número.'.format(n1))
    if n2 < n3:
        print('{} é o menor número.'.format(n2))
    else:
        print('{} é o menor número.'.format(n3))
if n2 > n1 and n2 > n3:
    print('{} é o maior número.'.format(n2))
    if n1 < n3:
        print('{} é o menor número.'.format(n1))
    else:
        print('{} é o menor número.'.format(n3))
if n3 > n1 and n3 > n2:
    print('{} é o maior número.'.format(n3))
    if n1 < n2:
        print('{} é o menor número.'.format(n1))
    else:
        print('{} é o menor número.'.format(n2))
print('=' * 64)