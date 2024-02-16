"""
Desafio 22

Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas
- O nome com todas minúsculas
- Quantas letras ao todo(sem considerar espaços)
- Quantas letras tem o primeiro nome

"""

print("{:=^40}".format(" Desafio 22 "))
nome = str(input("Nome completo: "))
print(nome.upper()) # Todas maiúsculas
print(nome.lower()) # Todas minúsculas
print("O seu nome possui {} letras".format(len(''.join(nome.split()))))
print("O seu primeiro nome tem {} letras".format(len(nome.split()[0])))
print("{:=^40}".format(""))