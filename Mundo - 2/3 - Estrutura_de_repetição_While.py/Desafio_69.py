'''
Crie um programa que leia a idade e o sexo de varias pessoas. 
A cada pessoa cadastrada o programa deverá perguntar se o usuario quer ou não continuar, no final mostre:

A - Quantas pessoas tem mais de 18 anos
B - Quantos homens foram cadastrados
C - Quantas mulheres tem menos de 20 anos
'''
maior_de_18 = homens_cadastrados = mulheres_menos_de_20 = 0
while True:
    print("-="*25)
    idade = int(input("Informe a idade: "))
    while True:
        sexo = str(input("Sexo [M | F]: ")).strip().upper()
        if sexo in 'MF':
            break
    print("Cadastro realizado com sucesso!")
    #Dados de saída
    if idade >= 18:
        maior_de_18 += 1
    if sexo in 'M':
        homens_cadastrados += 1
    if sexo in 'F' and idade < 18:
        mulheres_menos_de_20 += 1

    #Deseja continuar
    while True:
        cont = str(input("Deseja continuar [S | N]: ")).strip().upper()
        if cont in 'S':
            break
        elif cont in 'N':
            break
    if cont in 'N':
        break

#Imprimir os dados e saída
print("~"*40)
if maior_de_18 > 1:
    print(f"{maior_de_18} Pessoas são maiores de 18 anos")
else:
    print(f"{maior_de_18} Pessoa é maior de 18 anos")
if homens_cadastrados > 1:
    print(f"{homens_cadastrados} homens foram cadastrados")
else:
    print(f"{homens_cadastrados} homem foi cadastrado")
if mulheres_menos_de_20 > 1:
    print(f"{mulheres_menos_de_20} mulheres tem menos de 20 anos")
else:
    print(f"{mulheres_menos_de_20} mulher menor de 20 anos foram cadastradas")
print("~"*40)
        

    
            
    
    