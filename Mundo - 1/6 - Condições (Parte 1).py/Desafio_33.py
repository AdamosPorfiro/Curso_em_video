"""
Faça um programa que leia três numero e fale qual é o maior e qual é o menor
"""

n_1 = int(input("Informe o 1° número: "))
n_2 = int(input("Informe o 2° número: "))
n_3 = int(input("Informe o 3° número: "))
if n_1 > n_2 and n_2 > n_3:
    print("\n{} é o maior número\n{} é o menor número".format(n_1,n_3))
elif n_2 > n_1 and n_3 > n_1:
    print("\n{} é o maior número\n{} é o menor número".format(n_2,n_1))
elif n_3 > n_1 and n_1 > n_2:
    print("\n{} é o maior número\n{} é o menor número".format(n_3,n_2))
else:
    print("\n{} é o maior número\n{} é o menor número".format(n_1,n_2))
