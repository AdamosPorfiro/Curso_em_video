"""
Desafio 23

Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.

Ex: Digite um numero: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1

"""
print("{:=^40}".format(" Desafio 23 "))
num = str(input("Digite um numero entre 0 a 9999: ")) # Convertemos ele para string

# Manipulamos utilizando a técnica de fatiamento 
unidade = num[-1]
dezena = num[-2:-1]
centena = num[-3:-2]
milhar = num[-4:-3]

print("Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(unidade,dezena,centena,milhar))
print("{:=^40}".format(""))