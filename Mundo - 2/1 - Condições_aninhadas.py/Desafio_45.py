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
usuario = int(input("""Escolha 
    1- Pedra 
    2- Papel
    3- Tesoura
Opção: """))
user_dic = {1:'pedra', 2:'papel', 3:'tesoura'}

# Empate
if computador == 'pedra' and usuario == 1:
    print(f"Empatado!\nVocê escolheu {user_dic[1]} e o computador {computador}")
elif computador == 'papel' and usuario == 2:
    print(f"Empatado!\nVocê escolheu {user_dic[2]} e o computador {computador}")
elif computador == 'tesoura' and usuario == 3:
    print(f"Empatado!\nVocê escolheu {user_dic[3]} e o computador {computador}")


#Vencedor computador
elif computador == 'papel' and usuario == 1:
    print(f"Você perdeu!\nVocê escolheu {user_dic[1]} e o computador {computador}")
elif computador == 'tesoura' and usuario == 2:
    print(f"Você perdeu!\nVocê escolheu {user_dic[2]} e o computador {computador}")
elif computador == 'pedra' and usuario == 3:
    print(f"Você perdeu!\nVocê escolheu {user_dic[3]} e o computador {computador}")


#Vencedor jogador
elif computador == 'papel' and usuario == 3:
    print(f"Parabéns, você ganhou!\nVocê escolheu {user_dic[3]} e o computador {computador}")
elif computador == 'tesoura' and usuario == 1:
    print(f"Parabéns, você ganhou!\nVocê escolheu {user_dic[1]} e o computador {computador}")
  
elif computador == 'pedra' and usuario == 2:
    print(f"Parabéns, você ganhou!\nVocê escolheu {user_dic[2]} e o computador {computador}")

#Caso digite errado
else:
    print("Você deve digitar corretamente. Tente novamente!")
