'''
Faça um programa que leia o sexo de um pessoa, mas que só aceite M ou F. 
Caso esteja errado, peça a digitação novamente até ter um valor correto;
'''
s = ''
while s != 'M' and s != 'F':
    s = str(input('Sexo M/F: ')).upper().strip()
    if s != 'M' and s != 'F':
        print('Informação incorreta, Tente novamente!')
if s in 'Mm':
    print('Sexo masculino registrado com sucesso')
if s in 'Ff':
    print('Sexo feminino registrado com sucesso!')