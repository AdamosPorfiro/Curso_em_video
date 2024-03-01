"""
Faça um programa que calcule a soma de todos os numeros impares que são multiplos de três que se encontram no intervalo  de 1 até 500

"""
print("-="*20)
print("{:>25}".format(" Desafio 48 "))
print("-="*20)

soma = 0
qtd = 0

for c in range(1,501):
    if c % 2 != 0:
        if c % 3 == 0:
            soma += c
            qtd += 1
print(f"A soma de todos os {qtd} resulta no valor \33[1;32m{soma}\33[m")