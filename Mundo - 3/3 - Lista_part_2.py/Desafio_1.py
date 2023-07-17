'''
Faça um programa que leia o nome e peso de varias pessoas e guarde tudo em uma lista. No final mostre

a - Quantas pessoas foram cadastradas

b - Uma listagem com as pessoas mais pesadas

c - Uma listagem com as pessoas mais leve
'''
Armazenador = []
Nome_Peso = []
Cadastros = 0
while True:
    Armazenador.append(str(input('Digite o seu nome: ')))
    Armazenador.append(float(input('Digite o seu peso: ')))
    Nome_Peso.append(Armazenador[:])
    Armazenador.clear()
    Cadastros += 1
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

# Quantas pessoas foram cadastradas?
print(f'Quantidade de pessoas cadastradas: {Cadastros}')
