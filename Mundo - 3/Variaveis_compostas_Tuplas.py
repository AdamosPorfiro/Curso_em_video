'''
O que é uma tupla?
É uma estrutura de dados semelhante a ua lista, porém, com uma diferença fundamental:
A tupla é imutavel, signifiando que após os dados serem criados, eles não podem ser alterados.
Uma tupla é composta por elementos que são especialmente separados por virgula onde esses elementos
ficam dentro de parenteses ex:

tupla = (1,2,3,4,5)

Uma tupla pode armazenar valores, tipos diferentes, numeros, string, booleanos que podem ser acessados
por meio do indice ex:

Tupla = (1,2,3,4,5)
print(tupla[0]) = 1
print(tupla[2]) = 3

As tuplas são usadas quando deve possuir elementos que não podem ser modificados como coordenadas(x,y)
informações de data e hora e retornar multiplas informações de uma mesma função em um único objeto;

No novo python, versão mais recente, não é tão necessario colocar entre parenteses.
'''

Lanche = ('Hamburguer', 'Suco', 'Pizza', 'Puddin')
# Lanche[0] = 'Tacos'
print(Lanche)
print(Lanche[1])
print(Lanche[3])
print(Lanche[-1])
print(Lanche[1:3])
print(Lanche[2:])
print(Lanche[:2],'\n')

for pos,comida in enumerate(Lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi bastante!')
print('\n')
for cont in range(0, len(Lanche)):
    print(f'Eu vou comer {Lanche[cont]} na posição {cont}')
print('Comi bastante!\n')

print(sorted(Lanche),'\n') # Sorted - Coloca em ordem, ele converte para uma lista []

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a+b
print(a,'\n',b,'\n',c)
print(len(c))
print(c.count(5))
print(c.index(8))

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) # del - Deleta qualquer coisa feita no python, deleta!
print(pessoa)