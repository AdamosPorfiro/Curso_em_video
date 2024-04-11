"""
Crie um programa que leia nome, ano de nascimento e carteira
de trabalho e cadastre-os(com idade) em um dicionario. 
Se por acaso a CTPS for diferente de ZERO, o dicionario recebera
também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.

Considere que para se aposentar são 35 anos de contribuição
"""
from datetime import date
dados_ = {}
idade = anos_ctps = 0
while True:
    print("-"*17)
    dados_["nome"] = str(input("Nome: "))
    print("-"*17)
    dados_["ano_nascimento"] = int(input("Ano de nascimento: "))
    
    while True:
        print("-"*17)
        resp = int(input("Possui carteira de trabalho assinada [0 - Não | 1 - Sim]: "))
        if resp == 1:
            print("-"*17)
            dados_["ctps_ano"] = int(input("Ano de contratação: "))
            print("-"*17)
            dados_["ctps_salario"] = float(input("Salário: "))
            print("-"*17)
            break
        else:
            break
    break
if resp == 1:
    idade = date.today().year - dados_["ano_nascimento"]
    anos_ctps = date.today().year - dados_["ctps_ano"]
    print(f"Você possui {idade} anos.")
    print(f"Você vai se aposentar com {(35 - anos_ctps)+idade} anos.")