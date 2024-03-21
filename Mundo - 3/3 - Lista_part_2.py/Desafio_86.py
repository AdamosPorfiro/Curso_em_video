'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores
lidos pelo teclado, no final, mostre a matriz na tela. COm a formatação correta.
'''
matriz_1 = [[],[],[]]
matriz_2 = [[],[],[]]
matriz_3 = [[],[],[]]

for c in range(3):
    numero = int(input("Digite um valor: "))
    if matriz_1[0] == []:
        matriz_1[0] = numero
    elif matriz_1[1] == list([]):
        matriz_1[1] = numero
    elif matriz_1[2] == list([]):
        matriz_1[2] = numero
print(f"{matriz_1}")
               