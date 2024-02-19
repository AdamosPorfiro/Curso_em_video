"""
Desafio 23

Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.

Ex: Digite um numero: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1

"""
"""
# Formula utilizando string

print("{:=^40}".format(" Desafio 23 "))
num = str(input("Digite um numero entre 0 a 9999: ")) # Convertemos ele para string

# Manipulamos utilizando a técnica de fatiamento 
unidade = num[-1]
dezena = num[-2:-1]
centena = num[-3:-2]
milhar = num[-4:-3]

print("Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(unidade,dezena,centena,milhar))
print("{:=^40}".format(""))
"""
num = int(input("Informe um numero de 0 a 9999: "))
unidade = num // 1 % 10
dezenha = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10   
print("\nUnidade: {}".format(unidade))
print("Dezenha: {}".format(dezenha))
print("Centena: {}".format(centena))
print("Milhar: {}".format(milhar))