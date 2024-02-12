""" 
Desafio 14

Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

Formula:

F = (9/5)*c+32
"""

print("{:=^50}".format(" Desafio 14 "))
print("{:^50}".format(" Conversor de Celsius para Fahrenheit"))
temperatura = float(input("Informe a temperatura em graus C°: "))
conversor = (9/5)*temperatura+32
print("\n\nConvertendo...\nTemperatura em Fahrenheit: {}F°".format(conversor))
print("{:=^50}".format(""))