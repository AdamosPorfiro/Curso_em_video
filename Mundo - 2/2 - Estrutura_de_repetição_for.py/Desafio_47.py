"""
Crie um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50.

"""
print("-="*57)
print("{:>57}".format(" Desafio 47 "))
print("-="*57)
for c in range(1,51):
    if c % 2 == 0:
        print(c,end=' → ')
print("Acabou"+"\n"+"-="*57)