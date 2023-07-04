'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:

A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os numeros pares.
'''
Lista = []
Pares = []
qtd_9 = posicao_3 = 0
for c in range(4):
    n = int(input('Digite um numero: '))
    Lista.append(n)
converter_tupla = tuple(Lista)

for i, v in enumerate(converter_tupla):
    if v == 9:
        qtd_9+=1
    if v == 3 and posicao_3 == 0:
        posicao_3 = i+1
    if v % 2 == 0:
        Pares.append(v)
print(f'''Quantidade de valores 9 é: {qtd_9}\nPosição que 1º valor 3 está: {posicao_3}
Numeros pares digitados é: {Pares}''')