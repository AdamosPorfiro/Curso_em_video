"""
Desafio 15

Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

"""

dias = int(input("Por quantos dias o carro foi alugado?  "))
qtd_km = float(input("Quantos km foram rodados? "))
vl_dia = dias*60
vl_km = qtd_km*0.15
print("\n\nVocê alugou por {} dias.\nRodou {}km.\nO Valor total dos dias R$ {:.2f}\nO Valor total em km R$ {:.2f}\nO Total a pagar R$ {}".format(dias,qtd_km,vl_dia,vl_km,vl_dia+vl_km))