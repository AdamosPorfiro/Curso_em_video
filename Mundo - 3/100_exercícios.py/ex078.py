'''
Crie um programa onde o usuario passa a digitar varios valores númericos e cadastre-os em
uma lista. Caso o número já exista lá dentro, ele não será adicionado.

No final, serão exibidos todos os valores únicos digitados, em ordem crescente
'''
l_n = []
while True:
    n = int(input('Digite um número: '))
    if n in l_n:
        print('Esse número já existe na lista!', end=' ')
    else:
        l_n.append(n)
    c = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if c in 'S':
        continue
    else:
        break
l_n.sort()
print(f'Você digitou os números {l_n}')