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
        lista.append(for)
    variavel = lista[0]
    variavel = lista[0]
    for i lista
        if i > variavel
            variavel = i
    print i
'''
pesos=[]
for c in range(5):
    p = float(input('Informe o peso (kg): '))
    pesos.append(p)
p_maior = pesos[0]
p_menor = pesos[0]
for item in pesos:
    if item>p_maior:
        p_maior = item
    elif item<p_menor:
        p_menor=item
print('\nO maior peso é: {} kg\nO menor peso é: {} kg'.format(p_maior,p_menor))
