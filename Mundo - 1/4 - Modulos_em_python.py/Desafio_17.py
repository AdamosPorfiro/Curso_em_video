"""
Desafio 17

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo.
Calcule e mostre o comprimento da hipotenusa

"""
from math import hypot
cat_opo = float(input("Informe o cateto oposto: "))
cat_adj = float(input("Informe o cateto adjacente: "))
print("\nO cateto oposto é {}.\nO cateto adjacente é {}.\nA hipotenusa é {:.2f}.".format(cat_opo, cat_adj, hypot(cat_opo, cat_adj))) 