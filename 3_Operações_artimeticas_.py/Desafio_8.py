'''

===== Desafio 8 =====

Faça um programa que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

Analise criticamente: supondo que temos um produto no valor de R$ 120.0 e o desconto é de 5% o calculo é o seguinte:

Valor desconto = 120 * 5 = 600/100 = 6
R$ 6,00 é o equivalente a 5% de R$ 120,00

Metodo dos 5 Q's

1 - Quais são os dados de entrada?
-> input preço_produto.

2 - O que deve ser feito com esses dados?
-> fazer os calculos do preço no novo produto já com 5% de desconto e exibir na tela.

3 - Quais são as restrições do problema?
-> Como esse algoritmo tem entrada de dinheiro, ele vai trabalhar com casas decimais, ou seja numeros reais(float).

4 - Qual é o resultado esperado?
-> Mostrar para o usuario o novo preço do produto já com 5% de desconto.

5 - Quais são os passos necessarios para se alcançar o resultado?
#1 input preço_produto
#2 print preço_produto * 5 / 100 = Preço_com_desconto

'''
print('=' * 19, 'Desafio 8', '=' * 19)
v1 = float(input('\nDigite o preço do produto para calcular o desconto\nR$ '))
desconto = ((v1*5)/100)
print('\nO desconto é de: 5%\nO valor do desconto em reais é de: R$ {:.2f}\nO preço do produto com desconto é de:R$ {:.2f}'.format(desconto, v1 - desconto)+'\n','=' * 49)
