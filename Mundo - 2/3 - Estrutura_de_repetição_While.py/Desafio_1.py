'''
Faça um programa que leia o sexo de um pessoa, mas que só aceite M ou F. 
Caso esteja errado, peça a digitação novamente até ter um valor correto;
'''
s = ''
while s != 'M' and s != 'F': 
    s = str(input('Sexo M/F: ')).upper().strip()
    if s != 'M' and s != 'F':
        print('Informação incorreta, TENTE NOVAMENTE!')
if s == 'M':
    print('Masculino')
if s == 'F':
    print('Feminino')
    
'''if s in 'Mm':
    print('Masculino')
if s in 'Ff':
    print('Feminino')'''