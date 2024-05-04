"""
Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicioario e todos os
dicionarios em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média
"""

dados = dict()
dados_completo = list()
soma = divisor = valor_final = 0

while True:
    dados["nome"] = str(input("Nome: ")).capitalize().strip()
#------------------------------------------------------------------------
    while True:
        sexo = str(input("Sexo [M | F]: ")).upper().strip()
        if sexo == "M" or sexo == "F":
            dados["sexo"] = sexo
            break
#------------------------------------------------------------------------
    while True:
        idade = str(input("Idade: "))
        if idade.isdigit():
            dados["idade"] = int(idade)
            break
    dados_completo.append(dados.copy())
#------------------------------------------------------------------------
    while True:
        resp = str(input("Deseja continuar [S | N] ")).upper().strip()
        if resp == "S" or resp == "N":
            break
    if resp == "N":
        break
    print("-="*20)
print("-="*20)
#------------------------------------------------------------------------
#A) Quantas pessoas foram cadastradas
print(f"Foram cadastradas: {len(dados_completo[0:])} pessoas")
#------------------------------------------------------------------------
#B) A média de idade do grupo | A soma de todos os valores dividido pela quantidade de numeros.
for v in dados_completo:
    for r in v.values():
        if isinstance(r,(int)):
            divisor += 1
            soma += r
valor_final += (soma)/divisor
print(f"A média de idade do grupo é de: {valor_final:.0f} anos")
#------------------------------------------------------------------------
#C) Uma lista com todas as mulheres
print("-"*25)
print("\33[1;33mLista de mulheres\33[m")
for sexo in dados_completo:
    if sexo["sexo"] in "F":
        print(f"{sexo["nome"]}")
print("-"*25)
#------------------------------------------------------------------------
#D) Uma lista com todas as pessoas com idade acima da média
print("\33[1;33mPessoas acima da média de idade\33[m")
for i in dados_completo:
    if i["idade"] > valor_final:
        print(f"{i["nome"]} possui {i["idade"]} anos ")
print("-"*25)
