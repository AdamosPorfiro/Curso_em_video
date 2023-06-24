'''
Crie um programa que leia a idade e o sexo de varias pessoas. 
A cada pessoa cadastrada o programa deverá perguntar se o usuario quer ou não continuar, no final mostre:

A - Quantas pessoas tem mais de 18 anos
B - Quantos homens foram cadastrados
C - Quantas mulheres tem menos de 20 anos
'''

'''
Parte - 1
Para iniciar vamos criar um loop infinito  que vai rodar todo o programa
em seguida, mais dois loop's que vai receber os dados corretamente, idade e o sexo de varias pessoas 
O usuario deve informa os dados corretamente se não o loop é ativo;

'''
from time import sleep
Pessoasmaiores = qtd_homens = qtd_mulher_menor_20 = 0
print('{:=^25}\n{:>3}CADASTRO DE PESSOAS'.format('',''))
while True:
    while True:
        Idade = str(input('{:=^25}\nQual sua idade? '.format('')))
        if not Idade.isdigit():
            continue
        else:
            Idade = int(Idade) # Converte Idade para Int
            if Idade > 18: # Condição da opção opção (A) - Quantas pessoas tem mais de 18 anos
                Pessoasmaiores+=1
            break
    while True:
        Sexo = str(input('\nQual seu sexo [M/F]: ' )).upper().strip()[0]
        if Sexo in 'MF':
            if Sexo in 'M': # Condição da opção (B) - Quantos homens foram cadastrados
                qtd_homens+=1
            elif Sexo in 'F' and Idade < 20: # Condição da opção (C) - Quantas mulheres tem menos de 20 anos
                qtd_mulher_menor_20+=1
            break
        else:
            continue # Funcionou
        

# Parte - 2
# Vamos criar outro loop e condições que vão perguntar para o usuario se ele quer sair ou não!
#O usuario precisa dar a entrada correta, se não ele vai repetir o loop!
    while True:
        Sair_continuar = str(input('\nDeseja sair [S/N]: ' )).upper().strip()[0]
        if Sair_continuar not in 'SN':
            continue
        elif Sair_continuar in 'N':
            break
        elif Sair_continuar in 'S':
            break
    if Sair_continuar in 'S':
        print('\nAnalisando...')
        sleep(1)
        print(f'\nQuantidade de pessoas maiores de 18 anos: {Pessoasmaiores}.\nQuantidade de homens: {qtd_homens}.\nQuantidade de mulheres menores de 20 anos: {qtd_mulher_menor_20}.')
        break   #Funcionando    

        

    
            
    
    