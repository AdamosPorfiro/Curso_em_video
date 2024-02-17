"""
Desafio 22

Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas
- O nome com todas minúsculas
- Quantas letras ao todo(sem considerar espaços)
- Quantas letras tem o primeiro nome

"""
from time import sleep
print("{:=^40}".format(" Desafio 22 "))
nome = str(input("Nome completo: ")).strip()
print("\nAnalisando o seu nome...")
sleep(2.5)
print("O seu nome com todas as letras maiúsculas {}".format(nome.upper())) # Todas maiúsculas
print("O seu nome com todas as letras minúsculas".format(nome.lower())) # Todas minúsculas
print("O seu nome possui {} letras".format(len(''.join(nome.split())))) 
#print("O seu nome possui {} letras".format(len(nome) - nome.count(" "))) # 2°Opção
print("O seu primeiro nome é {} e possui {} letras".format(nome.split()[0],len(nome.split()[0]))) # 3º opção
#print("O seu primeiro nome tem {} letras".format(nome.find(" "))) # 2° opção
print("{:=^40}".format(""))