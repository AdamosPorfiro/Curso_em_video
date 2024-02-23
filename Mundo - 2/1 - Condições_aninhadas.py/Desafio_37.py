'''

Escreva um programa que leia um numero inteiro qualquer e peça para o usuario qual será a base
de conversão:

1 - para binário;
2 - para octal;
3 - para hexadecimal;
'''

from time import sleep
print("-="*27)
print("{:>38}".format("Conversor de base númerica"))
print("-="*27)
n1 = int(input("Informe um numero inteiro: "))
base = int(input(
"""Qual a base de conversão que deseja:
        1 - BINÁRIO
        2 - OCTAL
        3 - HEXADECIMAL
        Digite: """))
if base == 1:
    base = "BINÀRIO"
    n1 = bin(n1)
elif base == 2:
    base = "OCTAL"
    n1 = oct(n1)
elif base == 3:
    base = "HEXADECIMAL"
    n1 = hex(n1)
print("Convertendo dados...")
sleep(1.5)

print(f"O número convertido para {base} fica {n1}")
print("-="*27)