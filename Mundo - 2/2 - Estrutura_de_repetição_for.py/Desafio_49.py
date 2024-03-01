"""
Refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando um laço for
"""
print("-="*20)
print("{:>25}".format(" Desafio 49 "))
print("-="*20)
n = int(input("Numero que deseja saber a tabuada: "))
for c in range(1,11):
    #mult = c*n
    print(f"{c:2} x {n} = {c*n}")
print("-="*20)
