'''
Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

Analise critica: Vamos usar o modulo randon a função randint() para o computador pensar em um numero entre 0 e 5, depois
vamos pedir para o usuario tentar adivinhar que numero o computador pensou e depois usando uma estrutura de repetição definir
se o usuario venceu ou perdeu.

1 - Quais são os dados de entrada?
-> Variavel1 = randint(0,5);
-> input usuario;
-> estrutura de condição.

2 - Oque devo fazer com esses dados?
-> Computador vai usar variavel para armazenar o valor aleatório entre 0 e 5;
-> Vai ler imput do usuario;
-> Montar estrutura de condição que vai dizer se o usuario acertou ou não o numero que o computador gerou e armazenou.

3 - Quais são as restrições do problema?
-> Vai gerar um numero de 0 a 5 e armazena-lo;
-> O usuario vai ter que escolher um numero entre 0 e 5 ;
-> A estrutura de condição vai dizer se o usuario perdeu ou ganhou, com base na sua escolha.

4 - Qual o resultado esperado?
-> Que o computador gere e armazene um numero entre 0 e 5;
-> Ler o input do usuario e dizer se ele perdeu ou ganhou.

5 - Quais são os passos para se alcançar o resultado?
#1 - importar biblioteca randon a função randint(0,5) 
#2 - variavel_1 = randint(0,5)
#3 - input usuario
#4 - if input == variavel_1: Ganhou else: Perdeu
'''
print('=' * 7, 'Jogo de adivinhar', '=' * 7)
from random import randint
n = randint(0,5)
v = int(input('Escolha um numero entre 0 e 5: '))
if v == n:
    print('\nPARABÉNS, você acertou!')
else:
    print('\nQUE PENA, você errou\nO numero correto é: {}'.format(n))
print('=' * 33)