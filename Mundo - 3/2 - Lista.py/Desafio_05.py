'''
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores impares digitados
respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''
l_n = []
pares = []
impar = []
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
        impar.append(num)
print(f'\nVocê digitou os número {l_n}\nNúmeros pares são: {pares}\nNúmero ímpares são: {impar}')