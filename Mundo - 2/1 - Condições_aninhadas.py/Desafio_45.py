'''
Crie um programa que faça o computador jogar jokenpô com você;

Analisando: Jekenpô é uma brincadeira infantil que utiliza apenas as mãos e gestos simples
para determinar quem é vencedor;

Regras:

1 - Pedra ganha da tesoura;
2 - Papel ganha da pedra;
3 - Tesoura ganha do papel;

'''

from random import choice

lista = ['Pedra', 'Papel', 'Tesoura']
computador = choice(lista).lower()
usuario = str(input("Escolha Pedra, Papel ou Tesoura: ")).strip().lower()

# Empate
if computador == 'pedra' and usuario == 'pedra':
    print(f"Empatado!\nVocê escolheu {usuario} e o computador {computador}")
elif computador == 'papel' and usuario == 'papel':
    print(f"Empatado!\nVocê escolheu {usuario} e o computador {computador}")
elif computador == 'tesoura' and usuario == 'tesoura':
    print(f"Empatado!\nVocê escolheu {usuario} e o computador {computador}")


#Vencedor computador
elif computador == 'papel' and usuario == 'pedra':
    print(f"Você perdeu!\nVocê escolheu {usuario} e o computador {computador}")
elif computador == 'tesoura' and usuario == 'papel':
    print(f"Você perdeu!\nVocê escolheu {usuario} e o computador {computador}")
elif computador == 'pedra' and usuario == 'tesoura':
    print(f"Você perdeu!\nVocê escolheu {usuario} e o computador {computador}")


#Vencedor jogador
elif computador == 'papel' and usuario == 'tesoura':
    print(f"Parabéns, você ganhou!\nVocê escolheu {usuario} e o computador {computador}")
elif computador == 'tesoura' and usuario == 'pedra':
    print(f"Parabéns, você ganhou!\nVocê escolheu {usuario} e o computador {computador}")
  
elif computador == 'pedra' and usuario == 'papel':
    print(f"Parabéns, você ganhou!\nVocê escolheu {usuario} e o computador {computador}")

#Caso digite errado
else:
    print("Você deve digitar corretamente")