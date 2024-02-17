"""
Desafio 27

Faça um programa que leuia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
ultimo = Souza

"""
print("{:=^50}".format(" Desafio 27 "))
nome = str(input("Nome completo: ")).strip().split()
print("Primeiro nome é: {}".format(nome[0]))
print("Primeiro nome é: {}".format(nome[-1]))
print("{:=^50}".format(""))