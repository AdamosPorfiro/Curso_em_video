'''
Crie um programa que simule o funcionamento de um caixa eletronico.
No inicio, pergunte ao usuario qual será o valor a ser sacado (numero inteiro)
e o programa vai dizer quantas cedulas de cada valor serão entregues.

OBS: Considere que  o caixa possui cedulas de:
R$50 R$20 R$10 e R$1
'''
from time import sleep
print("-="*15)
print("{:>20}".format("Adamos bank"))
print("-="*15)

#Variaveis
nota_1 = nota_10 = nota_20 = nota_50 = 0

print("=>"*24)
print("Caixa possui notas de: R$50 | R$20 | R$10 | R$1")
saque = int(input("Qual o valor a ser sacado R$ "))
print("<="*24)
#Saque 50
while saque >= 50:
    nota_50 += 1
    saque -= 50

#Saque 20
while saque >= 20:
    nota_20 += 1
    saque -= 20

#Saque 10
while saque >= 10:
    nota_10 += 1
    saque -= 10

#Saque 1
while saque >= 1:
    nota_1 += 1
    saque -= 1

print("Quantidade de notas")
print(f"Sacando...")
sleep(1)
if nota_50 >= 1:
    print(f"{nota_50} notas de R$ 50")
if nota_20 >= 1:
    print(f"{nota_20} notas de R$ 20")
if nota_10 >= 1:
    print(f"{nota_10} notas de R$ 10")
if nota_1 >= 1:
    print(f"{nota_1} notas de R$ 1")
print("Volte sempre ao \33[0;34mADAMOS BANK\33[m! Tenha um bom dia!")


    







