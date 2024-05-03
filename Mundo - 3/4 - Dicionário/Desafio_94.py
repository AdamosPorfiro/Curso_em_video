"""
Crie um programa que leia nome, sexo e idade de varias pessoas,
guardando os dados de cada pessoa em um dicioario e todos os
dicionarios em uma lista. No final, mostre: 
A) Quatas pessoas foram cadastradas
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
print("Lista de mulheres")
for sexo in dados_completo:
    if sexo["sexo"] in "F":
        print(f"{sexo["nome"]}")
print("-"*25)
#------------------------------------------------------------------------
#D) Uma lista com todas as pessoas com idade acima da média
        
            

"""
dados_de_pessoas = dict()
dados_finais_das_pessoas = list()
mulheres = list()
total_cadastradas = 0

while True:
    dados_de_pessoas["nome"] = str(input("Nome: ")).capitalize().strip()
    dados_de_pessoas["sexo"] = str(input("Sexo [M | F]: ")).upper().strip()
    dados_de_pessoas["idade"] = int(input("Idade: "))
    total_cadastradas += 1
    dados_finais_das_pessoas.append(dados_de_pessoas.copy())
    dados_de_pessoas.clear()
    resp = str(input("Quer continuar [S | N]: ")).upper().strip()
    print("-="*10)
    if resp == "N":
        break
print(f"Total de pessoas cadastradas: {total_cadastradas}")
for r in dados_finais_das_pessoas:
    if r["sexo"] == "F":
        mulheres.append(r["nome"])
print(f"Lista de mulheres cadastradas:\n{mulheres}")
"""
        

