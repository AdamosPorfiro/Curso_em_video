'''
Crie um programa onde o usuario passa a digitar varios valores númericos e cadastre-os em
uma lista. Caso o número já exista lá dentro, ele não será adicionado.

No final, serão exibidos todos os valores únicos digitados, em ordem crescente
'''
l_n = []
while True:
    n = int(input('Digite um número: '))
    if n in l_n:
        print('Esse número já existe na lista!',end=' ')
    else:
        print('\nNúmero adicionado com sucesso...')
        l_n.append(n)
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'S':
        continue
    else:
        break
l_n.sort()
print(f'Você digitou os valores {l_n}')
