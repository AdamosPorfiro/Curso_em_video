'''
Faça um programa que o usuario jogue PAR ou ÍMPAR com o computador.
O jogo só será interronpido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
'''

'''
Parte - 1
Vamos iniciar o programa com um loop infinito que vai roda-lo varias vezes;
Inicialmente vamos desenvolver a escolha da maquina usando o modulo randon;
'''
from random import randint, choice
vencidas = empates = 0
print('\n{:=^28}\n{:>8}IMPAR OU PAR\n{:=^28}'.format('','',''))
while True:
    Numero_computador = randint(1,10)
    Lista = ['P','I']
    Escolha_computador = choice(Lista) # Funcionando

    '''
    Parte - 2
    Para a escolha do usuario, vamos iniciar com um loop infinito onde ele deve dar a entrada;
    dos dados corretamente, caso esteja errado o programa vai pedir para ele digitar corretamente;
    '''
    while True:
        Numero_usuario = int(input('Digite um número [1 á 10]: '))
        Escolha_usuario = str(input('Impar ou par [I/P]: ')).upper().strip()[0]
        if Numero_usuario < 1 or Numero_usuario > 10:
            continue
        if Escolha_usuario not in 'PI':
            continue
        else:
            break # Funcionando

    '''
    Parte - 3
    Vamos declarar o resultado do jogo e o contador de vitórias 
    para podermos comparar com os dados de entrada e contar partidas;
    '''
    Soma = Numero_computador+Numero_usuario
    Pi = ''

    if Soma % 2 == 0:
        Pi = 'P'
        #print(Pi[0],'\n',Escolha_computador, Escolha_usuario)
    else:
        Pi = 'I'
        #print(Pi[0],'\n',Escolha_computador, Escolha_usuario) # Funcionando

    '''
    Parte - 4
    Vamos criar condições que vai verificar se os dados de entrada são iguais, porém
    diferentes do resultado, sendo assim ninguem ganha
    '''
    if Escolha_computador in 'P' != Pi and Escolha_usuario in 'P' != Pi:
        print('\nNinguem ganhou\n')
    elif Escolha_computador in 'I' != Pi and Escolha_usuario in 'I' != Pi:
        print('\nNinguem ganhou\n') # Funcionando

 
    # Parte - 5
    # Vamos continuar as condições que vão verificar se os dados de entrada são iguais e que
    # tambem correspondem ambos ao resultado, sendo assim havendo um empate
    
    elif Escolha_computador in 'P' == Pi and Escolha_usuario in 'P' == Pi: # Empata com par
        print('\nEmpate\n')
        empates+=1
    elif Escolha_computador in 'I' == Pi and Escolha_usuario in 'I' == Pi: # Empata com impar
        print('\nEmpate\n')
        empates+=1
    
    # Parte - 6
    # Vamos continuar as condições dessa vez verificando se os dados entrada são diferentes um do outro e
    # se um deles corresponde ao resultado, se um deles corresponder então teremos um ganhador e um perdedor;
    
    elif Escolha_usuario in 'P' == Pi and Escolha_computador in 'I' != Pi: # Vence com par
        print('\nVocê venceu!\n')
        vencidas+=1
    elif Escolha_usuario in 'I' == Pi and Escolha_computador in 'P' != Pi: # Vence com impar
        print('\nVocê venceu!\n')
        vencidas+=1

    elif Escolha_usuario in 'P' != Pi and Escolha_computador in 'I' == Pi: # Perde com par
        print(f'\nVocê Perdeu!\nPartidas vencidas: {vencidas}.\nPartidas empatadas: {empates}.\n')
        break
    elif Escolha_usuario in 'I' != Pi and Escolha_computador in 'P' == Pi: # Perde com impar
        print(f'\nVocê Perdeu!\nPartidas vencidas: {vencidas}.\nPartidas empatadas: {empates}.\n')
        break
print('GAME OVER!')