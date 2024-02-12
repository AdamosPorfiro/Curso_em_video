"""

Desafio 6 

Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

5 Q's
1 - Quais são os dados de entrada?
    - Numero qualquer

2 - O que devo fazer com esses dados?
    - Mostrar na tela o dobro, triplo e a raiz quadrada do numero inteiro digitado

3 - Quais são as restrições desse programa?
    - O resultado é a operação multiplicação

4 - Qual é o resultado esperado?
    - Exibir na tela o dobro, triplo e raiz quadrada do numero informado

5 - Qual é a sequencia de passos a serem feitas?
    - import math
    - input numero
    - dobro = numero*2
    - triplo = numero*3
    -

"""
import math

print("{:=^28}".format(" Desafio 6 "))
n = int(input("Digite um numero: "))
dobro = n*2
triplo = n*3
quadrada = math.sqrt(n) #Para importar a função invocamos a função math seguido da operação a ser utilizada
print("\nDobro: {}\nTriplo: {}\nRaiz quadrada: {}\n".format(dobro,triplo,quadrada))
print("{:=^28}".format(""))
