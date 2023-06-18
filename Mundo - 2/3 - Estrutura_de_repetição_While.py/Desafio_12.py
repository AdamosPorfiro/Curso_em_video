'''
Faça um programa que o usuario jogue PAR ou ÍMPAR com o computador.
O jogo só será interronpido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.

Dados de entrada: 
input usuario_numero, input usuario_P_I;
randint(1,10) computador, choice[PAR, IMPAR] computador

O que fazer com esses dados: 
Somar os numeros escolhidos;
Verificar se o resultado da soma é PAR ou IMPAR;
Comparar a escolha do usuario e do computador com a verificação PAR/IMPAR;
Se ambas as escolhas forem iguais a verificação PAR/IMPAR então é empate e a partida continua;
Se a escolha do usuario for correspondente a verificação PAR/IMPAR ele vence e a partida continua,
se não ele perde e a partida é interronpida;
Quando a partida for interrompida p placar do usuario é exibido;

Restrições:
Escolha dos números é de 1 á 10;

Resultado:
O úsuario jogue PAR ou ÍMPAR com o computador, se o usuario perder o jogo é interrompido;

Passo a passo:
while True:
    computador_numero = randint(1,10)
    computador_lista = [PAR, IMPAR]
    escolha_computador = choice(computador_lista)

    input numero_usuario
    input par_impar_usuario
    soma = computador_numero + numero_usuario
    verificação_i_p = ''
    contador_usuario empate = 0
    if s % 2
        verificação_i_p = PAR
    else:
        verificação_i_p = ÍMPAR
    if par_impar_usuario == verificação_i_p == escolha_computador
        print empate!
        empate+=1
    elif par_impar_usuario == verificação_i_p and escolha_computador != verificação_i_p
        print você ganhou!
        contador_usuario+=1
    else
        print você perdeu!
        break
print Venceu {Contador_usuario}
print Empatou {empate}
print Game Over!
'''
from random import randint, choice
quantidade_vencidas = 0
while True:

    #Escolhas do computador
    lista = ['P', 'I']
    computador_n = randint(1,10)
    computador_e = choice(lista)

    #Escolha do usuario
    while True:
        n1 = int(input('Digite um numero [1 á 10]: '))
        if n1 < 1 or n1 > 10:
            continue
        n2 = str(input('Ímpar ou Par [I/P]: ')).upper()[0].strip()
        if n2 not in 'PI':
            continue
        elif n2 in 'PI':
            break

    #Comparar os resultados para encontrar o vencedor
    resultado_1 = computador_n + n1

    # Variavel IMPAR e PAR
    Par = ''
    Impar = ''

    # Calculando Par e Impar
    if resultado_1 % 2 == 0 :
        Par = 'P'
    elif resultado_1 % 2 == 1:
        Impar = 'I' 

    #Empate com PAR
    if Par in 'P' and computador_e  == Par and n2[0]  == Par:
        quantidade_vencidas += 1
        print(f'\nEMPATOU.\nSoma: {resultado_1} = PAR.\nJogadas: jogador PAR x Computador PAR.')
    
    #Empate com IMPAR
    elif Impar in 'I' and computador_e  == Impar and n2[0]  == Impar:
        quantidade_vencidas += 1
        print(f'\nEMPATOU.\nSoma: {resultado_1} = IMPAR.\nJogadas: jogador IMPAR x Computador IMPAR.')
       
    # Jogador ganhar PAR
    elif Par in 'P' and n2 [0] == Par and computador_e  != Par:
        quantidade_vencidas += 1
        print(f'\nPARABENS!!! Você ganhou!.\nSoma: {resultado_1} = PAR.\nJogadas: jogador PAR x Computador IMPAR.')
     
     # Jogador ganhar IMPAR
    elif Impar in 'I' and n2 [0] == Impar and computador_e != Impar:
        quantidade_vencidas += 1
        print(f'\nPARABENS!!! Você ganhou!.\nSoma: {resultado_1} = IMPAR.\nJogadas: jogador IMPAR x Computador PAR.')
    
    #Comutador ganhar PAR
    elif Par in 'P' and computador_e == Par and n2[0] != Par:
        print(f'\nGAME OVER!.\nResultado: {resultado_1} = PAR.\nJogadas: jogador IMPAR x Computador PAR.\nPartidas vencidas consecutivas: {quantidade_vencidas}')
        break
    elif Impar in 'I' and computador_e == Impar and n2[0] != Impar:
        print(f'\nGAME OVER!.\nSoma: {resultado_1} = PAR.\nJogadas: jogador PAR x Computador IMPAR.\nPartidas vencidas: {quantidade_vencidas} Partidas.')
        break
    


       
  

    

