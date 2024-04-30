"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No
final mostre o conteúdo da estrutura na tela.
"""
situacao = dict()

situacao["nome"] = str(input("Nome: ")).capitalize()
situacao["media"] = float(input("Média: "))

print()
print(f"="*20)
print(f"{"Nome":<10}{"Média":>8}")    
print(f"{situacao['nome']:<10}{situacao['media']:>7}")
print(f"="*20)

"""
print(f"{situacao.values()}")#Exibir apenas os valores dentro do dicionario
print(f"{situacao.keys()}")#Exibir apenas o nome das chaves
print(f"{situacao.items()}")#Exibir os dois "values" e "keys"
"""

