"""
Refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando um laço for
"""
print('\n'+'{: ^5}{}'.format('','Tabuada'))
n1 = int(input("Informe um numero: "))
for c in range(1, 11):
    print("{} x {:2} = {:3}".format(n1, c, n1 * c))
print('{:=^20}'.format(''))