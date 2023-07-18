'''
Faça um programa que leia o nome e peso de varias pessoas e guarde tudo em uma lista. No final mostre

a - Quantas pessoas foram cadastradas

b - Uma listagem com as pessoas mais pesadas

c - Uma listagem com as pessoas mais leve
'''
Armazenador = []
Nome_Peso = []
Cadastros  = 0
pesos = []
n_maior_p = ''
while True:
    Armazenador.append(str(input('Digite o seu nome: ')))
    Armazenador.append(float(input('Digite o seu peso: ')))
    Nome_Peso.append(Armazenador[:])
    Armazenador.clear()
    Cadastros += 1
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
while True:
    for c in Nome_Peso:
        if c[1] > pesos[:-1]:
            pesos.append(c[1])
    for p in pesos:
            if c[1] > p:
                pesos.append(c[1])

# Quantas pessoas foram cadastradas?
print(f'Quantidade de pessoas cadastradas: {Cadastros}.')
# Listagem pessoas mais pesadas
print(f'O maior é peso é do(a) {n_maior_p} com {peso} kg.')
