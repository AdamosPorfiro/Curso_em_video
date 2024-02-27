'''
A confedereção nacional de natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: Mirim;
- Até 14 anos: Infantil;
- Até 19 anos: Junior;
- Até 20 anos: Sênior;
- Acima: Master.

'''
print("-=" * 20)
print("{:>25}".format(" Desafio 41 "))
print("-=" * 20)
from datetime import date
ano_nasc = int(input("Informe o ano de nascimento: "))
ano = date.today().year - ano_nasc

if ano <= 9:
    categoria = "MIRIM"
elif ano <= 14:
    categoria = "INFATIL"
elif ano <= 19:
    categoria = "JUNIOR"
elif ano == 20:
    categoria = "SÊNIOR"
else:
    categoria = "MASTER"
print(f"Você tem {ano} ano e sua categoria é \33[1;32m{categoria}\33[m")
print("-=" * 20)