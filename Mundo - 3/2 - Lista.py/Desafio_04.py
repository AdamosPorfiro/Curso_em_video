'''
Crie um programa que vai ler varios numeros e colocar em uma lista.

 Depois disso, mostre:

 A) Quantos números foram digitados

 B) A lista de valores, ordenada de forma descrescente

 C) Se o valor 5 foi digitado e está ou não na lista
'''
l_n = []
while True:
    n = int(input('Digite um número: '))
    l_n.append(n)
    c = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if c in 'S':
        continue
    else:
        break
l_n.sort(reverse=True)
print(f'\nForam digitados {len(l_n)} números\nOrdem decrescente {l_n}')

numero = False
for num in l_n:
    if num == 5:
        numero = True
        break
if numero == True:
    print('O número 5 está ná lista!')
else:
    print('O número 5 não está na lista!')