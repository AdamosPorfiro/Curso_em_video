'''
Melhore o jogo do DESAFIO  onde o computador vai pensar em um numero entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até, acertar, mostrando no final quantos
palpites foram necessarios para vencer.

Metodo dos 5 q's

1 - Quais são os dados de entrada?
input computador
input palpite_usuario

2 - O que devo fazer com esses dados?
Deve compara-lo com os dados armazenados pelo computador e exibir na tela se o usuario
acertou o palpite

3 - Quais são as restrições do problema?
 Computador vai pensar em um numero apenas de 1 a 10
 Jogador vai dar um palpite até acertar

4 - Qual é o resultado esperado?
O computador deve pensar em um numero armazenar, o usuario deve dar um palpite sobre
o numero pensado pelo computador, caso ele acerte uma mensagem de ganhou irá aparecer e
se ele deseja continuar ou não o jogo, caso erre uma mensagem de perdeu irá aparecer e
se ele deseja continuar ou não o jogo. 

5 - Quais são os passos para se alcançar o resultado esperado?
Vamos importar a biblioteca random e função radint;
usaremos radint para que o computador selecione um numero entre 0 e 10
Esse numero será armazenado em uma variavel n;
contador_de_palpite = 0
continuar = 'S'
while continuar in 'Ss'
    input usuario
    if palpite_usuario != n
        contador_de_palpite += 1
        input continuar Deseja continuar [S/N]
'''
from random import randint,seed
continuar = ''
print ('\n{:=^33}\n{:^5}JOGO ADIVINHE O NÚMERO\n{:^3}Dê um palpite entre 0 á 10'.format('','','',''))
while continuar in 'Ss':
    contador = 0
    p = ''
    n = randint(0,10)
    while p != n:
        contador += 1
        p = int(input('{:=^33}\nPalpite: '.format('')).strip())
    if p == n:
        print('\nPARABÉNS!!!Você acertou!\nQuantidade de palpites: {}'.format(contador))
        continuar = str(input('Deseja continuar jogando? [S/N]: ')).strip().upper()
        while continuar != 'S' and continuar != 'N':
            continuar = str(input('Deseja continuar jogando? [S/N]: ')).strip().upper()
        if continuar in 'nN':
            print('Obrigado por jogar!')
        



