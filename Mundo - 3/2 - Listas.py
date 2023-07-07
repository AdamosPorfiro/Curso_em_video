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
lanche.pop(3) - Geralmente usado eliminar o ultimo elemento da lista, porém pode passar como parametro o que voce deseja eliminar.
lanche.remove(valor que quer eliminar)  - Vai eliminar o elemento, a chave reposiciona as chaves.

Podemos tambem criar listas através de ranges:
valor = list(range(4,11)) - Usamos uma função conhecida como 'lista' e podemos usar range para criar essa lista, nesse caso ele vai 
criar uma lista de 4 a 11 - valor = 4,5,6,7,8,9,10,11.

É possivel ordenar os elementos de uma lista usando a função sort(). No caso da lista acima
valor.sort() - Vai ordenar todos os valores
valor.sorte(reverse=True) - Ordena os valores, porém inverte a ordem. 
'''

