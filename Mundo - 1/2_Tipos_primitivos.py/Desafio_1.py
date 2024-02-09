#Crie um programa que leia dois numeros e mostre a soma deles

print ('===== Desafio 1 =====')
n1 = (input('Digite um numero: '))
n2 = (input('Digite mais um numero  para soma-los: '))
"""print("Valor digitado é numerico? ", n1.isnumeric())
print("Valor digitado é numerico?",n2.isnumeric())"""
resultado = int(n1) + int(n2)
print ('A soma de {} + {} = {}' .format (n1, n2, resultado))