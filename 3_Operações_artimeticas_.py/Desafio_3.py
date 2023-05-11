'''
===== Desafio 3 =====

Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

Metodo 5 Q's

1 - Quais são os dados de entrada?
 -> input n1;
 -> input n2.

2 - O que deve ser feito com esses dados?
 -> Deve calcular e mostrar sua média.
     Para calcular a media você soma o conjunto de numero e divide pela quantidade de numeros que possem no conjunto Ex.: 2+5+6+7=20/4=5

3 - Quais são as restrições desse problema?
 -> Média geralmente trabalha com numero reais de preferência.

4 - Qual o resultado esperado?
 -> Calcular e exibir na tela a média do aluno.

5 - Quais são os passos para se alcançar o resultado?
#1 - input nota1
#2 - input nota2
print A sua média é: ().

'''

print('\n'+'=' * 6, 'Desafio 3', '=' * 6,'\n',' ' * 2, 'Calculadora média')
nota1 = int(input('\nDigite a primeira nota:\nNota 1: '))
nota2 = int(input('\nDigite a segunda nota:\nNota 2: '))
print ('\nA sua média é: {}'.format((nota1 + nota2)/2),'\n'+'=' * 23)
