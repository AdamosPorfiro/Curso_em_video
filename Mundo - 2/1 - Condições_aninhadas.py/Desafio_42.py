'''
Refaça o desafio 035 dos triangulos acrescentando o recurso de mostrar que tipo
de triangulo será formado:

- Equilátero: Todas os lados iguais;
- Isosceles: Dois lados iguais;
- Escaleno: Todos os lados diferentes;

Enunciado do ex035: 

Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem
ou não formar um triângulo.

Ex.:

R1 - -------- 
R2 - -------------
R3 - -----------------

===============================================================================
Desigualdade triangular:

Diz que para formar um triangulo com três retas é necessario que duas retas, sejam maiores que a terceira, logo se
obtemos:

A|B|C então:
A + B > C = True;
A + C > B = True;
B + C > A = True;

1|2|3
1 + 2 >= 3 True;
1 + 3 >= 2 True;
2 + 3 >= 1 True;
CASO ESSAS REGRAS SEJAM ATENDIDAS, ENTÃO PODEMOS TER UM TRIANGULO COM TRÊS RETAS.

Equilátero:
1 - Todas as retas devem possuir o mesmo comprimento;
CASO ESSA REGRA SEJA ATENDIDA, ENTÃO PODEMOS TER UM ISOSCELE.

Isosceles:
1 - Pelo menos duas retas devem ter o mesmo comprimento;
2 - A soma de duas retas resulta em um numero maior que a medida da terceira;
CASO ESSAS REGRAS SEJAM ATENDIDAS, ENTÃO PODEMOS TER UM ISOSCELES.

Escaleno: 
1 - Todas as retas devem ter comprimentos diferentes; 
2 - A soma de duas retas devem ser maior que a terceira;
CASO ESSAS REGRAS SEJAM ATENDIDAS, ENTÃO PODEMOS TER UM ESCALENO.

- Equilátero: Todas os lados iguais;
- Isosceles: Dois lados iguais;
- Escaleno: Todos os lados diferentes;
=================================================================================

'''
print("-="*20)
print("{:>23}".format("Desafio 42"))
print("-="*20)
r1 = float(input("Informe o comprimento da 1° reta: "))
r2 = float(input("Informe o comprimento da 2° reta: "))
r3 = float(input("Informe o comprimento da 3° reta: "))

#Triângulo
if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    #Equilatero
    if r1==r2 and r1==r3 and r2==r3:
        print("É possível formar um EQUILÁTERO")
    #Isosceles
    elif r1==r2  or r1==r3 or r2==r3:
        if r1+r2>r3 or r1+r3>r2 or r2+r3>r1:
            print("É possível formar um ISOSCELES")
    #Escaleno
    elif r1!=r2 and r1!=r3 and r2!=r3:
        if r1+r2>r3 or r1+r3>r2 or r2+r3>r1:
            print("É possível formar um ESCALENO")
else:
    print("Não é possível formar um triangulo")
print("-="*20)
    