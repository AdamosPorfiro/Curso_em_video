'''
Faça um programa que leia 5 valores númericos e guarde em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

Lembrando que caso algum numero seja repetido ele vai mostrar a posição de ambos os valores. 
'''

lista_de_valores = []
maior = 0
posição_maior = []
posição_menor = []

for c in range(0,5):
    num = int(input("Digite um número inteiro: "))
    lista_de_valores.append(num)

menor = lista_de_valores[0]
#=====================================================
for pos in range(0,len(lista_de_valores)):
    #Maior
    if lista_de_valores[pos] > maior:
        maior = lista_de_valores[pos]
    #Menor
    if lista_de_valores[pos] < menor:
        menor = lista_de_valores[pos]
#======================================================
    #Posição
for pos, num in enumerate(lista_de_valores):
    #Maior
    if num == maior:
        posição_maior.append(pos+1)
    #Menor
    if num == menor:
        posição_menor.append(pos+1)
    
        
print(f"Os valore digitado foram {lista_de_valores}")
print(f"O maior elemento é \33[1;34m{maior}\33[m na posição {posição_maior}")
print(f"O menor elemento é \33[1;34m{menor}\33[m na posição {posição_menor}")
