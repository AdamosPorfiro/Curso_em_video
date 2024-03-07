'''
Faça um programa que o usuario jogue PAR ou ÍMPAR com o computador.
O jogo só será interronpido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
'''
from time import sleep
from random import randint,choice
escolha_computador = ['I','P']
Jogadas = empates = 0
while True:

    #Computador
    computador = randint(1,10)
    escolha_computador = choice(escolha_computador)
    
    #Jogador
    print("-="*15)
    jogador = int(input("Digite um número [0 á 10]: "))
    escolha_jogador = str(input("Escolhar Ímpar ou Par [I | P]: ")).strip().upper()
    while escolha_jogador not in 'PÍI':
        escolha_jogador = str(input("Digite corretamente, Ímpar ou Par [I | P]: ")).strip().upper()
        if escolha_jogador in 'PÍI':
            break
    print("-="*15)
    
    #Verificação para definir vencedor, perdedor ou empate  
    if escolha_computador == 'P':
        escolha_computador = "PAR"
    else:
        escolha_computador = "ÍMPAR"

    if escolha_jogador == 'P':
        escolha_jogador = "PAR"
    else:
        escolha_jogador = 'ÍMPAR'
   

    soma = computador + jogador
    if soma % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "ÍMPAR"

    #Resultado
    print(f"Computador escolheu o número {computador} e o jogador {jogador}")
    print(f"A soma fica {computador} + {jogador} = {soma}\nO número {soma} é {resultado}")
    print("~"*30)
    print(f"O jogador escolheu {escolha_jogador} e o computador escolheu {escolha_computador}")
    print("~"*30)

    #Computador vende
    if escolha_computador == resultado and escolha_jogador != resultado:
        print(f"Venceu {Jogadas} vezes e Empatou {empates} vezes")
        print("Você perdeu! GAME OVER")
        continuar = str(input("Quer tentar novamente [S | N]: ")).strip().upper()
        if continuar in 'N':
            break
    #Jogador vence
    elif escolha_jogador == resultado and escolha_computador != resultado:
        Jogadas +=1
        print(f"Parabens, Você VENCEU {Jogadas} vezes e empatou {empates} vezes")
    #Empate
    elif escolha_computador == resultado and escolha_jogador == resultado:
        empates += 1
        print(f"Empatado, Você empatou {empates} vezes")
    else:
        print("Ninguem ganhou!!!")
print("Fechando o jogo...")
sleep(1.5)
