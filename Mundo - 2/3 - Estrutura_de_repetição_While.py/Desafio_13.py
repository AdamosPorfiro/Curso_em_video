'''
Crie um programa que leia a idade e o sexo de varias pessoas. 
A cada pessoa cadastrada o programa deverá perguntar se o usuario quer ou não continuar, no final mostre:

A - Quantas pessoas tem mais de 18 anos
B - Quantos homens foram cadastrados
C - Quantas mulheres tem menos de 20 anos
'''

'''
Parte - 1
Para iniciar vamos criar um loop infinito  que vai receber a idade e o sexo de varias pessoas
'''

while True:
    Idade = int(input('Qual sua idade? '))
    Sexo = str(input('Qual seu sexo [M/F]: ')).upper().strip()[0]

# Parte - 2
# Vamos criar uma condição que vai perguntar para o usuario se ele quer sair ou não!

    Sair_continuar = str(input('Deseja sair [S/N]: ')).upper().strip()[0]
    if Sair_continuar not in 'SN':
        continue
    if Sair_continuar in 'N':
        continue
    if Sair_continuar in 'S':
        break       # Funcionou   
    