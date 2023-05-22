#Crie um programa que leia dois numeros e mostre a soma deles

print ('\n'+'=' * 10, 'Exercício 3','=' * 10 + '\n','Calculadora soma de dois números')
n1 = int(input('\nDigite um numero inteiro\nNumero:\033[31m '))
n2 = int(input('\033[m\nDigite outro numero inteiro\nNumero:\033[31m  '))
print ('\033[m\nA soma de {}{}{} + {}{}{} = {}{}{}' .format ('\033[31m',n1,'\033[m','\033[31m', n2,'\033[m','\033[32m', n1 + n2,'\033[m'))