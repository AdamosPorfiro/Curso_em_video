'''
Crie um programa que simule o funcionamento de um caixa eletronico.
No inicio, pergunte ao usuario qual será o valor a ser sacado (numero inteiro)
e o programa vai dizer quantas cedulas de cada valor serão entregues.

OBS: Considere que  o caixa possui cedulas de:
R$50 R$20 R$10 e R$1
'''
from time import sleep
print("-="*15)
print("{:>20}".format("Adamos bank"))
print("-="*15)
nota_1 = nota_10 = Nota_20 = 0

while True:
    print("\nCaixa possui notas de: R$50 | R$20 | R$10 | R$1")
    saque = int(input("Qual o valor a ser sacado R$ "))
"""
    # Saque de 1 a 9
    if saque <= 9:
        for c in range(saque,0,-1):
            nota_1 += 1
            if c == 0:
                break
        if nota_1 == saque:
            break
"""
    
print("\nSacando...")
sleep(0.5)
if saque <= 9:
    print(f"Você vai receber {nota_1} notas de R$ 1")
if saque >= 10 and saque <= 49:
    print(f"Você vai receber {nota_10} notas de R$ 1")






