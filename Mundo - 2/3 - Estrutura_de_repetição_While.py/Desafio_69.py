'''
Crie um programa que leia a idade e o sexo de varias pessoas. 
A cada pessoa cadastrada o programa deverá perguntar se o usuario quer ou não continuar, no final mostre:

A - Quantas pessoas tem mais de 18 anos
B - Quantos homens foram cadastrados
C - Quantas mulheres tem menos de 20 anos
'''

while True:
    print("-="*25)
    idade = int(input("Informe a idade: "))
    sexo = str(input("Sexo [M | F]: ")).strip().upper()
    while True:
        continuar = str(input("Deseja continuar [S | N]: ")).strip().upper()
        if continuar in 'S':
            break
        elif continuar in 'N':
            break
        print("-="*25)
        break
    if continuar in 'N':
        break
    

    
            
    
    