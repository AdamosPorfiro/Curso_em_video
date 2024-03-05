'''
Faça um programa que leia o sexo de um pessoa, mas que só aceite M ou F. 
Caso esteja errado, peça a digitação novamente até ter um valor correto;
'''
sexo = ' '
while sexo not in 'MF':
    sexo = str(input("Qual o seu sexo [M | F]: ")).upper().strip()
    if sexo not in 'MF':
        print("OPS, erro!!! Digite corretamente!")
if sexo in "M":
    print("Sexo masculino registrado com sucesso!")
if sexo in "F":
    print("Sexo feminino registrado com sucesso!")