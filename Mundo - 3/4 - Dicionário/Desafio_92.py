"""
Crie um programa que leia nome, ano de nascimento e carteira
de trabalho e cadastre-os(com idade) em um dicionario. 
Se por acaso a CTPS for diferente de ZERO, o dicionario recebera
também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.

Considere que para se aposentar são 35 anos de contribuição
"""
dados_ = dict()
dados_copy = list()

while True:
    dados_["nome"] = str(input("Nome: "))
    dados_["ano_nascimento"] = int(input("Ano de nascimento: "))
    dados_["ctps"] = str(input("Possui carteira de trabalho assinada [S/N]"))

