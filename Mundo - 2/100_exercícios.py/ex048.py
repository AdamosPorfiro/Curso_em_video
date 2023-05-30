"""
Faça um programa que calcule todo os numeros impares que são multiplos de três e que se encontram no intervalo  de 1 até 500

O que são numero impares multiplos por três?
R: Numeros ímpares  é um numero que quando é dividido por 2 o seu resto resulta em 1 Ex: 3%2=1
E numero impares multiplos de três é quando o numero impar que é divido perfeitamente por 3 o resto da sua divisão resulta em 0 Ex: 3%3 = 0

"""
for con in range(1, 501):
    if con % 2 == 1 and con % 3 == 0:
        print("{:3} = {} {}".format(con, con % 3,'Logo, esse valor é impar multiplo de 3'))
