'''
Faça um programa que o usuario jogue PAR ou ÍMPAR com o computador.
O jogo só será interronpido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
'''

from random import randint,choice
escolha_computador = ['I','P']
while True:

    #Computador
    computador = randint(1,10)
    escolha_computador = choice(escolha_computador)
    
    #Jogador
    print("-="*15)
    jogador = int(input("Digite um número [0 á 10]: "))
    escolha_jogador = str(input("Escolhar Ímpar ou Par [I | P]: ")).strip().upper()
    
    if escolha_computador == 'P':
        escolha_computador = "PAR"
    else:
        escolha_computador = "ÍMPAR"

    if escolha_jogador == 'P':
        escolha_jogador = "PAR"
    else:
        escolha_jogador = 'ÍMPAR'
    print("-="*15)

    soma = computador + jogador
    if soma % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "ÍMPAR"

    #Resultado
    print(f"Computador escolheu o número {computador} e o jogador {jogador} a soma fica {soma}\nO número {soma} é {resultado}")
    print(f"O jogador escolheu {escolha_computador} e o computador escolheu {escolha_jogador}")

    #Computador vende
    if escolha_computador == resultado and escolha_jogador != resultado:
        print("Você perdeu! GAME OVER")
        continuar = str(input("Quer tentar novamente [S | N]: "))
        if continuar in 'N':
            break
    #Jogador vence
    elif escolha_jogador == resultado and escolha_computador != resultado:
        print("Parabens, Você VENCEU!")
    #Empate
    elif escolha_computador == resultado and escolha_jogador == resultado:
        print("Empatado")
