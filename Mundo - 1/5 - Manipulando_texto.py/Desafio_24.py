"""
Desafio 24

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

"""
print("{:=^30}".format(" Desafio 24 "))
Name_city = str(input("Digite o nome da cidade: ")).upper() # Receber do usuario
Separar = Name_city.split() # Separo a string
Começa = Separar[0] in "SANTO" # Valido os dados se cidade começa ou não com SANTO
Dicionario = {True: "Sim", False: "Não"} # Uso mapeamento de dicionario para mapear a validação
print("A cidade começa com SANTO? {}".format(Dicionario[Começa])) # Exibo o resultado para o usuario
print("{:=^30}".format(""))