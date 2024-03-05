'''
Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um numero entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até, acertar, mostrando no final quantos
palpites foram necessarios para vencer.
'''

from random import randint

print("-="*20)
print("{:>25}".format(" Desafio 60 "))
print("-="*20)
#Escolha do computador
computador = randint(0,10)

Qtd_palpites = jogador = 0

while jogador != computador:
    #Escolha jogador
    jogador = int(input("Adivinhe o númnero sorteado pelo computador [0 á 10]: "))
    Qtd_palpites += 1
    if jogador > computador:
        print("Errou! É menor\n")
    elif jogador < computador:
        print("Errou! É maior\n")
#Venceu
print(f"\nParabens, pensei no número {computador}\nVocê acertou com {Qtd_palpites} palpites")