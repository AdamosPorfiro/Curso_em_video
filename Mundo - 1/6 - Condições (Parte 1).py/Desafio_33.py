"""
Faça um programa que leia três numero e fale qual é o maior e qual é o menor
"""

print("{:=^30}".format(" Desafio 33 "))
n1 = int(input("Informe o 1° número: "))
n2 = int(input("Informe o 2° número: "))
n3 = int(input("Informe o 3° número: "))

if n1>n2 and n2>n3:
    print("{} é maior e {} é menor".format(n1,n3))
elif n1>n3 and n3>n2:
    print("{} é maior e {} é menor".format(n1,n2))
elif n2>n1 and n1>n3:
    print("{} é maior e {} é menor".format(n2,n3))
elif n2>n3 and n3>n1:
    print("{} é maior e {} é menor".format(n2,n1))
elif n3>n1 and n1>n2:
    print("{} é maior e {} é menor".format(n3,n2))
else:
    print("{} é maior e {} é menor".format(n3,n1))
print("{:=^30}".format(""))