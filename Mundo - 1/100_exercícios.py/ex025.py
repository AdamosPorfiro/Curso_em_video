'''
Crie um programa que leie o nome de uma pessoa e diga se ela tem "Silva" no nome

n = str(input('Nome completo: '))
n1 = n.lower()
if("silva" in n1):
    print('Sim, o seu nome possui silva')
else:
    print('Não, o seu nome não possui silva')
    
'''

n = str(input('Nome completo: ')).strip()
min = n.lower()
print('\nAnalisando nome: {}...\nPossui silva no nome: {}'.format(n, "silva" in min))