'''
Faça um programa que leia o sexo de um pessoa, mas que só aceite M ou F. 
Caso esteja errado, peça a digitação novamente até ter um valor correto;
'''
sexo = ' '
while sexo not in 'MF':
    sexo = str(input("Qual o seu sexo [M | F]: ")).upper()
    if sexo not in 'MF':
        print("OPS, erro!!! Digite corretamente!")
print("Acabou!")