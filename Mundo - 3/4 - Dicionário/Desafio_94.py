"""
Crie um programa que leia nome, sexo e idade de varias pessoas,
guardando os dados de cada pessoa em um dicioario e todos os
dicionarios em uma lista. No final, mostre: 
A) Quatas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média
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

        

