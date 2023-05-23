'''
===== Exercicio 10 =====

Crie um programa que mostre quanto dinheiro uma pessoa tem na carteira e quantos dolares ela pode comprar.
Considere: U$ 1.00 = R$ 3.27

Analise critica:
- Vamos supor que possuimos o valor de R$ 50,00 e a cada R$ 3.27 conseguimos comprar U$ 1.00, quantos dolares conseguimos comprar?
- Vamos fazer uma divisão rapida, onde iremos dividir o valor que possuimos R$ 50,00 pela cotação do dolar que é de R$ 3,27, o resultado será: R$ 15.29

1 - Quais são os dados de entrada?
-> input dinheiro_carteira

2 - O que devo fazer com esses dados?
-> Ler quantos reais a pessoa tem na carteira e dizer quantos dolares ela pode comprar.

3 - Quais são as restrições desse problema?
-> Numeros reais

4 - Qual é o resultado esperado?
-> Quantos dolares é possível comprar com o dinheiro que a pessoa possui.

5 - Qual a sequência de passos a ser feita para se alcançar o resultado?
#1  input dinheiro_carteira
#2  print dinheiro_carteira / 3.27

'''

print('=' * 19, 'Exercício 10', '=' * 19,'\n', ' ' * 9 ,'Conversor de real para dolar')
d1 = float(input('\nQuanto dinheiro você possui para converter em dolar?\n'))
print ('\nVocê possui: R${} reais.\nPode adquirir: U${:.2f} dólares'.format(d1, d1 / 3.27))
print('=' * 50)