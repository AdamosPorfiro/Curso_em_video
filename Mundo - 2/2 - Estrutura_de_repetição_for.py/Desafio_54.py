'''
Crie um programa que leia o ano de nascimento de 7 pessoas. 
No final diga quantas pessoas ainda não atingiram maioridade e quantas já são maiores.

Ex: 21 anos

'''
print("-="*15)
print("{:>20}".format(" Desafio 54 "))
print("-="*15)
from datetime import date

qdt_pessoas = 0
for c in range(1,8):
    nasc = int(input("Informe o ano de nascimento: "))
    if date.today().year-nasc >= 21:
        qdt_pessoas += 1
print(f"\n{qdt_pessoas} pessoas são maiores de idade")
print("-="*15)
