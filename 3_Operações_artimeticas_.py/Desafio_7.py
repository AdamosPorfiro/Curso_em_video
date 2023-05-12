'''

===== Desafio 7 =====

Faça um programa que leia a largura e altura  de uma parede em metros, calcule a sua area e a 
quantidade de tinta necessaria para pinta-la, sabendo que cada 1 litro de tinta pinta uma area de 2m².

Analisar criticamente: Vamos somar a largura e a altura de uma parede e armazenar esse valor que será usado para calcular a quatidade
de tinta necessaria para pintar essa parede: Supondo que 1 liro de tinta pinte uma area de 2m² e temos uma parede com largura de 5 metros
de largura e 3 metros de altura 5x3, para descobrir a quantidade de tinta vamos fazer a soma da AxL= altura e largura = 8 metros de parede e
em seguida dividir pelo tamanho da area que a que 1 litro de tinta é capaz de pintar 2m²: 5+3*8/2= 4 Litros de tinta para pintar uma area de 8 metros

Metodo 5 Q's

1 - Quais são os dados de entrada?
-> input largura;
-> input altura.

2 - O que devo fazer com esses dados?
-> Ler os dados para calcular em metros a sua area total e em seguida dizer quantos litros de tinta será necessario para pintar aquela area.

3 - Esse problema possui alguma restrição?
-> Calculado em m² logo os numeros com decimais, reais, flutuantes.

4 - Qual é o resultado esperado?
-> Calcular a area total da parede e exibir para o usuario quantos litros de tinta serão necessarios para pintar essa area.

5 - Quais são os passos necessarios para se alcançar o resultado?
#1 input largura;
#2 input altura;
#3 print altura + largura / 2 = quantidade de tinta necessaria para pintar a area desejada.

'''

print('\n'+'=' * 30, 'Desafio 7', '=' * 30,'\n', ' ' * 20, 'Calculadora de tintas M²')
a1 = float(input('\nDigite a largura da parede\n'))
l1 = float(input('\nDigite a altura da parede\n'))
print('\nÁ area total da parede é de: {} metros\nA quantidade de tinta necessaria para pinta-lá é de: {:.3f} litros de tinta'.format(a1 * l1, (a1 * l1) /2)+'\n'+'=' * 72)