"""
Desafio 11

Faça um programa que leia a largura e a altura em metros, calcule a sua area e a quantidade de tinta necessaria para pintá-la, sabendo que
cada litro de tinta pinta uma área de 2m².

"""
print("{:=^40}".format(" Desafio 11 "))
l = float(input("Informe a largura da parede: "))
a = float(input("Informe a altura da parede: "))
area = l*a
qtd_tinta = area/2
print("\nArea total: {} m²\nQuantidade de tinta: {} litros".format(area,round(qtd_tinta)))
print("{:=^40}".format(""))