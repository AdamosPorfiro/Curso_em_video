'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:

A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os numeros pares.

Lista = []
Pares = []
qtd_9  = indice_3 = 0
for c in range(4):
    n = int(input('Digite um numero: '))
    Lista.append(n)
convert_tupla = tuple(Lista)

for indice,valor in enumerate(convert_tupla):
    if valor == 9:
        qtd_9+=1
    if valor == 3 and indice_3 == 0:
        indice_3 = indice + 1 
    if valor % 2 == 0:
        Pares.append(valor)
print(f''Você digitou os valores: {convert_tupla}\nO valor 9 apareceu: {qtd_9} vezes\nA posição que o primeiro 3 foi digitado foi: {indice_3}
Os numeros pares são: {Pares}'')
'''
n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),         
     int(input('Digite mais um número: ')),
     int(input('Digite um útilmo número: ')))
print(f'\nOs valores digitados foram: {n}')
print(f'O número 9 foi digitado {n.count(9)} vezes')
if 3 in n:
    print(f'O número 3 está na {n.index(3)+1}º posição')
else:
    print('O número 3 não foi digitado!')
print('Os números pares digitados foram: ', end='')
for c in n:
    if c % 2 == 0:
        print(f'{c} ', end='')