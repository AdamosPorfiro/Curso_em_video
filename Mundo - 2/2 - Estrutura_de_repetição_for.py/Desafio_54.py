'''
Crie um programa que leia o ano de nascimento de 7 pessoas. 
No final diga quantas pessoas ainda não atingiram maioridade e quantas já são maiores.

Ex: 21 anos

'''
print("-="*15)
print("{:>20}".format(" Desafio 54 "))
print("-="*15)
from datetime import date

qdt_pessoas_maiores = 0
qdt_pessoas_menores = 0
for c in range(1,8):
    nasc = int(input(f"Em que ano a {c}° pessoa nasceu: "))
    if date.today().year-nasc >= 21:
        qdt_pessoas_maiores += 1
    elif date.today().year-nasc < 21:
        qdt_pessoas_menores += 1
print(f"\n{qdt_pessoas_maiores} pessoas são maiores de idade")
print(f"\n{qdt_pessoas_menores} pessoas são menores de idade")
print("-="*15)
