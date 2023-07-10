'''
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores impares digitados
respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''

l_n = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    l_n.append(n)
    c = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if c in 'S':
        continue
    else:
        break
for num in l_n:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f'\nNúmeros digitados foram {l_n}\nOs pares são {pares}\nÍmpares são {impares}')