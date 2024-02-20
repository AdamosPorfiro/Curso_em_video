"""
Desafio 35

Desenvolva um programa que leia o comprimento de 3 retas e vai dizer 
se ele pode ou não formar um triangulo

"""
print("{:=^40}".format(" Desafio 35 "))
r1 = float(input("Informe comprimento da 1º reta: "))
r2 = float(input("Informe comprimento da 1º reta: "))
r3 = float(input("Informe comprimento da 1º reta: "))


if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print("\nSim é possível formar um triângulo")
else:
    print("\nNão é possível formar um triângulo")
print("{:=^40}".format(""))
"""
if r1+r2>r3:
    if r1+r3>r2:
        if r2+r3>r1:
            print("\nPode sim formar um triângulo!")
        else:
            print("\nNão é possivel formar um triângulo")
    else:
        print("\nNão é possivel formar um triângulo")
else:
    print("\nNão é possivel formar um triângulo")
"""