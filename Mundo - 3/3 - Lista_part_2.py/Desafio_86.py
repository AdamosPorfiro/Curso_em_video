'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores
lidos pelo teclado, no final, mostre a matriz na tela. COm a formatação correta.
'''
matriz_1 = [[],[],[]]
matriz_2 = [[],[],[]]
matriz_3 = [[],[],[]]

for c in range(9):
    numero = int(input("Digite um valor: "))
    #Matriz 1
    if matriz_1[0] == []:
        matriz_1[0].append(numero)
    elif matriz_1[1] == []:
        matriz_1[1].append(numero)
    elif matriz_1[2] == []:
        matriz_1[2].append(numero)
    #Matriz 2
    if c >= 3:
        if matriz_2[0] == []:
            matriz_2[0].append(numero)
        elif matriz_2[1] == []:
            matriz_2[1].append(numero)
        elif matriz_2[2] == []:
            matriz_2[2].append(numero)
    #Matriz 3
    if c >= 6:
        if matriz_3[0] == []:
            matriz_3[0].append(numero)
        elif matriz_3[1] == []:
            matriz_3[1].append(numero)
        elif matriz_3[2] == []:
            matriz_3[2].append(numero)
#----------------------------------------------- Exibição
for numero in matriz_1:
    print(numero,end=' ')
print("")
for numero in matriz_2:
    print(numero,end=' ')
print("") 
for numero in matriz_3:
    print(numero,end=' ')    
               