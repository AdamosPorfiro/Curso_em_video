"""
Desafio 15

Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

"""

print("{:=^40}".format(" Desafio 15 "))
dias = int(input("Por quantos dias o carro foi alugado?  "))
qtd_km = float(input("Quantos km foram rodados? "))
Total = dias*60+qtd_km*0.15

print("\nTotal a pagar R$ {}".format(Total))
print("{:=^40}".format(""))