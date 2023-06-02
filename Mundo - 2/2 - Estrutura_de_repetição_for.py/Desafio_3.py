"""
Faça um programa que calcule todo os numeros impares que são multiplos de três e que se encontram no intervalo  de 1 até 500

O que são numero impares multiplos por três?
R: Numeros ímpares  é um numero que quando é dividido por 2 o seu resto resulta em 1 Ex: 3%2=1
E numero impares multiplos de três é quando o numero impar que é divido perfeitamente por 3 o resto da sua divisão resulta em 0 Ex: 3%3 = 0

"""
soma = 0
cont = 0
for c in range(1, 501,2):
    if c % 3 == 0:
        soma = soma+c
        cont = cont+1
print('\nPossui {} impares multiplos de três\nA soma desses numeros fica {}'.format(cont, soma))
        