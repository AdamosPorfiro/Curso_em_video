'''
Faça um programa que leia o nome e um nascimento de um jovem e informe de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar;
- Se já passou do tempo do alistamente;

Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo.

'''

from datetime import datetime
nome = str(input("Nome: "))
dia_nasceu = int(input("Informe o dia em que nasceu:  "))
mes_nasceu = int(input("Informe o mês em que nasceu:  "))
ano_nasceu = int(input("Informe o ano em que nasceu:  "))

if datetime.today().year - ano_nasceu < 18:
    print("\nVocê não completou 18 anos ainda, volte quando completar 18 anos.\nPara mais informações acesse: https://alistamento.eb.mil.br/")
elif datetime.today().year - ano_nasceu == 18 and datetime.today().month <= mes_nasceu and datetime.today().day >= dia_nasceu:
    print("\nParabéns, está na hora de você se alistar, acesse o site e se faça sua candidatura: https://alistamento.eb.mil.br/")
elif datetime.today().year - ano_nasceu > 18:
    print("\nVocê já passou do tempo de alistamento acesse o site para mais informações: https://alistamento.eb.mil.br/") 