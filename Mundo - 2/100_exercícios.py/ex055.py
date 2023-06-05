'''
Faça um programa que leia o peso de 5 pessoas. No final mostre qual é o maior e o menor peso lidos.

Analise:
- Lista para armazenar os inputs
- For para repetir e armazenar o input 5x
- for que vai passar por cada item da lista
- cria uma variavel para ter como paramentro o valor maior e menor, elas são inicializada com o primeiro item da lista [0]
- condicional que vai exibir o maior item da 

Quais são os dados de entrada?
input peso 5x

O que devo fazer com esses dados?
Devo armazenar em uma lista, ler os dados e exibir qual foi o maior e o menor valor lido

Quais são as restrições desse problema?
Pesos possuem decimais, float
Qual é o maior e qual é o menor

Qual é o resultado esperado?
Exibir qual o peso maior e o menor lidos

Quais são os passos para se alcançar o resultado?
    lista = []
    for (5)
        input Informe o peso (Kg):
    variavel = lista[0]
    for i lista
        if i > variavel
            variavel = i
    print i
'''
lista=[]
for c in range(1,6):
    p = float(input('Informe o peso da {}° pessoa (kg): '.format(c)))
    lista.append(p)
valor_maior = lista[0]
valor_menor = lista[0]
for item in lista:
    if item>valor_maior:
        valor_maior = item
    elif item<valor_menor:
        valor_menor=item

print('\nO maior peso é: {:.1f} kg\nO menor peso é: {:.1f} kg'.format(valor_maior, valor_menor))



