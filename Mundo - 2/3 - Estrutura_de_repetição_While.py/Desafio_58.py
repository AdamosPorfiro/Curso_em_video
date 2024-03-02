'''
Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um numero entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até, acertar, mostrando no final quantos
palpites foram necessarios para vencer.
'''

from random import randint

#Escolha do computador
computador = randint(0,10)

Qtd_palpites = jogador = 0

while jogador != computador:
    #Escolha jogador
    jogador = int(input("Adivinhe o númnero sorteado pelo computador [0 á 10]: "))
    Qtd_palpites += 1
    if jogador > computador:
        print("Pensei em um número menor\n")
    elif jogador < computador:
        print("Pensei em um número maior\n")
#Venceu
print(f"\nParabens, pensei no número {computador}\nVocê fez {Qtd_palpites} palpites")