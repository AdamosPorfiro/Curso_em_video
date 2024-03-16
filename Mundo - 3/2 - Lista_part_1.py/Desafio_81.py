'''
Crie um programa que vai ler varios numeros e colocar em uma lista.

 Depois disso, mostre:

 A) Quantos números foram digitados

 B) A lista de valores, ordenada de forma descrescente

 C) Se o valor 5 foi digitado e está ou não na lista
'''
numeros = []
qtd_numeros = numero_5 = 0
while True:
    n = int(input("Digite um número: "))
    numeros.append(n)
    numero_5 += 1
    qtd_numeros += 1
    while True:
        sair = str(input("Deseja sair [S|N]: ")).strip().upper()
        if sair not in 'SN':
            continue
        elif sair in 'S':
            break
        elif sair in 'N':
            break
    if sair in 'N':
        break
print(f"Foram digitados {qtd_numeros} números")
numeros.sort(reverse=True)
print(numeros)
for pos, item in enumerate(numeros):
    if item[pos] == '5':
        print(f"Sim, o número 5 está na lista na posição {pos}")
        break
    else:
        print("Não, o número 5 não está na lista")