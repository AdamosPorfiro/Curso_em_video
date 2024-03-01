"""
Crie um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50.

"""
print("-="*35)
print("{:>40}".format(" Desafio 47 "))
print("-="*35)
for c in range(1,51):
    if c % 2 == 0:
        print(c,end=' ')
print("\n"+"-="*35)