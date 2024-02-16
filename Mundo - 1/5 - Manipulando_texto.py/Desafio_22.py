"""
Desafio 22

Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas
- O nome com todas minúsculas
- Quantas letras ao todo(sem considerar espaços)
- Quantas letras tem o primeiro nome

"""

print("{:=^45}".format(" Desafio 22 "))
nome = str(input("Nome completo: "))
print(nome.upper()) # Todas maiúsculas
print(nome.lower()) # Todas minúsculas
nome = nome.split()
print("O primeiro nome tem {} letras".format(len(nome[0])))
nome = ''.join(nome)
print("O nome completo possui {} letras".format(len(nome)))
print("{:=^45}".format(""))