'''
Faça um programa que leia o peso de 5 pessoas. No final mostre qual é o maior e o menor peso lidos.

'''
print("-="*20)
print("{:>25}".format(" Desafio 55 "))
print("-="*20)
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input("Informe o seu peso: "))
    if peso > maior:
       maior = peso
    if menor == 0:
        menor = peso
    if peso < menor:
        menor = peso
print(f"o maior peso é de {maior} kg")
print(f"o menor peso é de {menor} kg")
print("-="*20)
