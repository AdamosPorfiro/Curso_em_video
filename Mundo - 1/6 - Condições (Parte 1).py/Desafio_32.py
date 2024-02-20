"""
Desafio 32

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

1° passo - Um ano é bissexto quando é divisivel por 4
2° passo -  Se ele é divisivel por 100 e não por 400 não é bissexto
3° passo -  Um ano que é divisivel por 400 ele é bissexto
"""
from datetime import datetime

print("{:=^40}".format(" Desafio 32 "))

ano = int(input("Informe o ano que deseja verificar ou 0 para verificar o ano atual: "))
if ano == 0:
    ano = datetime.today().year    
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print(f"\nO ano {ano} é bissexto")
else:
    print(f"\nO ano {ano} não é bissexto!")    
print("{:=^40}".format(""))

"""
if  ano%4 == 0:
    if ano%100 == 0: 
        if ano%400 == 0:
            print("O ano {} é bissexto!".format(ano))
        else:
            print("O ano {} não é bissexto!".format(ano))
    else:
        print("O ano {} é bissexto!".format(ano))
"""