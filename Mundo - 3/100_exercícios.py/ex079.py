"""
Crie um programa onde o usuario pode digitar cinco valores númericos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort())

No final, mostre a lista ordenada na tela.
"""

l_n = []
for c in range(5):
    n = int(input('Digite um número: '))
    if l_n == 0:
        l_n.append(n)
    else:
        indice = 0
        while indice < len(l_n) and n > l_n[indice]:
            indice += 1
        l_n.insert(indice, n)
print(f'Os número digitados foram {l_n}')    