""" 
Desafio 5

Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e o seu antecessor

Metodo dos 5 Q's

1 - Quais são os dados de entrada?
 - Numero inteiro

2 - O que devo fazer com esses dados?
 - Mostrar na tela o seu sucessor e o seu antecessor

3 - Quais são as restrições desse problemas?
 - Deve ser numero inteiro

4 - Qual é o resultado esperado?
 - Exibir para o usuario o sucessor e o antecessor do numero informado

5 - Qual é a sequencia de passos a serem feitas?
 - Input numero
 - V_1 = numero - 1
 - V_2 = numero + 1
 - Print o sucessor do numero informado é V_1 e o seu antecessor é V_2

"""

print("{:=^28}".format(" Desafio 5 "))
n_1 = int(input("Digite um numero inteiro: "))
sucessor = n_1 + 1
antecessor = n_1 - 1
print("O sucessor de {} é {}\nO antecessor de {} é {}".format(n_1,sucessor,n_1,antecessor))
print("{:=^28}".format(""))
