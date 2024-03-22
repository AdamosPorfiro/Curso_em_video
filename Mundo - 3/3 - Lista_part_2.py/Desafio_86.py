'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores
lidos pelo teclado, no final, mostre a matriz na tela. COm a formatação correta.
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
print("Matriz 3x3")
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