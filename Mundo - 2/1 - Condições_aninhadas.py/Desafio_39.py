'''
Faça um programa que leia o nome e um nascimento de um jovem e informe de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar;
- Se já passou do tempo do alistamente;

Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo.

'''

from datetime import date
nome = str(input("Nome: "))
ano_nasceu = int(input("Ano de nascimento:  "))
idade = date.today().year - ano_nasceu

if idade < 18:
    saldo = 18 - idade
    print(f"\nVocê tem apenas {idade}.\nFaltam {saldo} anos para você completar 18 anos.\nVolte no ano de {date.today().year+saldo} para se alistar\nPara mais informações acesse: https://alistamento.eb.mil.br/")
elif idade == 18:
    print(f"\nParabéns, você tem {idade} anos e está na hora de você se alistar.\nDirija-se a um posto e aliste-se\nAcesse o site e se faça sua candidatura: https://alistamento.eb.mil.br/")
elif idade > 18:
    saldo = idade - 18
    print(f"\nVocê tem {idade} anos e já passou {idade - 18} anos.\nEra para você se alistar no ano de {date.today().year - saldo} vá a um posto e aliste-se.\nAcesse o site para mais informações: https://alistamento.eb.mil.br/") 