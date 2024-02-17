"""
Desafio 25

Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
"""
print("{:=^35}".format(" Desafio 25 "))
nome = str(input("Nome completo: ")).upper()
nome = nome.count("SILVA")
dicionario = {1: "Sim", 0: "Não"}
print("Possui SILVA no nome? {}".format(dicionario[nome]))
print("{:=^35}".format(""))