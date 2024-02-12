"""
Desafio 12

Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento

"""

print("{:=^50}".format(" Desafio 13 "))
salario = float(input("Informe o salario R$ "))
aumento_s = ((salario*15)/100)+salario
print("\nO seu salario teve um aumento de 15%. Agora voce recebe R$ {:.3f}".format(aumento_s))
print("{:=^50}".format(""))