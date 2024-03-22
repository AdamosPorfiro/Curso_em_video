'''
Aprimore o desafio anterior, mostrando no final:

a - A soma de todos os valores pares digitados

b - A soma dos valores da terceira coluna

c - O maior valor da segunda linha
'''

matriz = [[],[],[],[],[],[],[],[],[]]

for c in range(9):
    numero = int(input("Digite um valor: "))
    #Matriz 1
    if matriz[0] == []:
        matriz[0].append(numero)
    elif matriz[1] == []:
        matriz[1].append(numero)
    elif matriz[2] == []:
        matriz[2].append(numero)
    elif matriz[3] == []:
        matriz[3].append(numero)
    elif matriz[4] == []:
        matriz[4].append(numero)
    elif matriz[5] == []:
        matriz[5].append(numero)
    elif matriz[6] == []:
        matriz[6].append(numero)
    elif matriz[7] == []:
        matriz[7].append(numero)
    elif matriz[8] == []:
        matriz[8].append(numero)
    elif matriz[9] == []:
        matriz[9].append(numero)
#----------------------------------------------- Exibição
print("="*20)
for numero in range(len(matriz)):
    if numero >= 0 and numero <= 2:
        print(matriz[numero], end=' ')
    if numero == 2:
        print("")
    if numero >= 3 and numero <= 5:
        print(matriz[numero], end=' ')
    if numero == 5:
        print("")
    if numero >= 6 and numero <= 8:
        print(matriz[numero], end=' ')  
print("")
print("="*20)
#----------------------------------------------- Soma pares
soma = 0
pares = []
for numero in matriz:
    for n in numero:
        if n % 2 == 0:
            soma += n
            pares.append(n)
print(f"A Soma dos valores pares da matriz é {soma}, sendo: {pares}")
#----------------------------------------------- Soma da terceira coluna
soma_terceira_coluna = 0
if matriz[2] != []:
    for c in matriz[2]:
        soma_terceira_coluna += c
if matriz[5] != []:
    for c in matriz[5]:
        soma_terceira_coluna += c
if matriz[8] != []:
    for c in matriz[8]:
        soma_terceira_coluna += c
print(f"A soma da terceira coluna é de {soma_terceira_coluna}")
#----------------------------------------------- O maior valor da segunda linha
maior_valor = matriz[3]
if maior_valor < matriz[4] and matriz[4] > matriz[5]:
    maior_valor = matriz[4]
if maior_valor < matriz[5] and matriz[5] > matriz[4]:
    maior_valor = matriz[5]
print(f"O maior valor da segunda coluna é {maior_valor}")
