'''

===== Exercício 13 =====

Faça um programa que leia o salario de um funcionario e mostre o seu novo salario, com 15% de aumento.

Analise criticamente:
Supondo que o profissional seja balconista e recebe R$ 1.300 por mês e terá um aumento de R$ 15% *Sonho meu :_) kkkkkkkk*
Vamos então multiplicar o salario pelo aumento e dividir por 100, o resultado é o valor que terá de aumento no salario:

1300*15/100 = 195 - logo o aumento é de R$ 195 reais, basta então somar  1300 + 195 = 1495
Para validar se o valor de 195 equivale a 15% de 1300, basta fazer o calculo: porcentagem = 195 / 1300 = 0.15 * 100 = 15 % logo 195 equivale a 15% de 1300

Metodo dos 5 Q's

1 - Quais são os dados de entrada?
-> input salario

2 - O que deve ser feito com esses dados?
-> Calcular o salario com um aumento de 15% e exibir na tela

3 - Quais são as restrições desse problema?
-> Como os dados serão numeros com decimais o programa deve trabalhar com numeros reais (float)

4 - Qual o resultado esperado?
-> Que o programa calcule o salario com aumento de 15% e exiba para o usuario esse aumento.

5 - Quais são os passos a serem feitos para se alcançar o resultado?
#1 input salario
#2 print salario é: salario * 15 / 100 + salario

'''
print('=' * 18, 'Exercício 13', '=' * 19, '\n','Calculadora de 15 porcento de aumento no salario')
s1 = float(input('\nDigite o seu salario mensal\n'))
print('\nO seu novo salario é: R$ {:.2f}'.format((s1 * 15) / 100 + s1))
print('=' * 51)