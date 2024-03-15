'''
Variaveis compostas - Listas
O que são listas?
É uma variavel composta em pytohn, que permite armazenar varios elementos em uma única estrutura. É uma lista ordenada
de elementos, onde cada elemento pode ser de qualquer tipo de dado. Elas são definidas por comchetes [ ], e nesse caso
diferente de uma tupla que é imutavel, a lista ela é sim multavel conforme o necessario.

Para adicionar um elemento a lista usamos o comando .append ex: n.append(2) lista n vai receber o elemento 2.
Para inserir um elemento entre algum elemento da lista usamos o metodo insert(0,'algo'), onde 0 é o elemento onde você vai adicionar 
o elemento desejado.

Para apagar elementos usamos del ou usando pop
del lance[3]
lanche.pop(3) - Geralmente usado eliminar o ultimo elemento da lista, porém pode passar como parâmetro o que voce deseja eliminar.
lanche.remove(valor que quer eliminar)  - Vai eliminar o elemento, a chave se reposiciona

Podemos tambem criar listas através de ranges:
valor = list(range(4,11)) - Usamos uma função conhecida como 'lista' e podemos usar range para criar essa lista, nesse caso ele vai 
criar uma lista de 4 a 11 - valor = 4,5,6,7,8,9,10.

É possivel ordenar os elementos de uma lista usando a função sort(). No caso da lista acima
valor.sort() - Vai ordenar todos os valores
valor.sort(reverse=True) - Ordena os valores, porém inverte a ordem. 

num = [2,5,9,1]
num[2] = 3 # Não é possivel alterar uma tupla, pois ela é imutavel.
num.append(7) # Vai adicionar o valor 7 a lista num. Tabem já é adicionado uma nova chave para esse elemento
num.sort(reverse=True) # Vai ordenar os numeros de forma reversa.
num.insert(1, 2) # Vai adicionar na posição 2 o elemento 0, lembrando que as chaves são organizadas automaticamente
num.pop() # Se usarmos a função pop() sem parametro, ela vai eliminar o ultimo elemento da lista.
num.pop(3) # Vai eliminar o elemento 2 que no caso é o elemento 0 que adicionamos interiormente.
if 4 in num:    
    num.remove(4) # Ele reomvoe apenas o primeiro elemento que corresponde ao parametro que nesse caso é 2
else:
    print('Não encontramos o numero 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')]


valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(0,5):
    valores.append(int(input('Digite um número: ')))
for c,v in enumerate(valores):
    #print(f'{v}...', end='')
    print(f'Na posição {c} encontramos o valor {v}')
print('Cheguei no final da lista')

a = [2,3,4,7]
b = a
b[2] = 8
print(f'Lista A: {a}\nLista B: {b}') # Quando as listas são igualadas, elas criam uma ligação, caso 1 seja alterada a outra tambem será alterada.

a = [2,3,4,7]
b = a[:] # Nesse caso ele não cria uma ligação, mas sim uma cópia
b[2] = 8
print(f'Lista A: {a}\nLista B: {b}')
'''
