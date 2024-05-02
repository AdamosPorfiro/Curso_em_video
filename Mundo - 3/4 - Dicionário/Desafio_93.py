"""
Crie um programa que gerencie o aproveitamento de um jogador
de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols
feitos em cada partida. No final, tudo isso será guardado em um
dicionário incluindo o total de gols feitos durante o campeonato
"""

Jogador = dict()
Partidas = list()


Jogador["nome"] = str(input("Nome jogador: "))
tot = int(input(f"Quantas partidas o jogador {Jogador["nome"]} jogou? "))
for c in range(0, tot):
    Partidas.append(int(input(f"Quantos gols na partida {c+1}°? ")))
Jogador["Gols"] = Partidas[:]
Jogador["Total"]= sum(Partidas)

print("-="*30)
print(f"{Jogador}")
print("-="*30)

for k,v in Jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("-="*30)

print(f"O jogador {Jogador["nome"]} jogou {len(Jogador["Gols"])} partidas")
for i, v in enumerate(Jogador["Gols"]):
    print(f"    => Na partida {i+1} fez {v} gols.")
print(f"Foi um total de {Jogador["Total"]} gols.")

    

        
