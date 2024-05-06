"""
Aprimore o desafio 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

Jogador = dict()
Partidas = list()

Jogadores = list()

while True:
    Jogador["nome"] = str(input("Nome jogador: "))
    tot = int(input(f"Quantas partidas o jogador {Jogador["nome"]} jogou? "))
#--------------------------------------------------------------------------------------
    for c in range(0, tot):
        Partidas.append(int(input(f"Quantos gols na partida {c+1}°? ")))
    Jogador["Gols"] = Partidas[:]
    Jogador["Total"]= sum(Partidas)
    Jogadores.append(Jogador.copy())
    Jogador.clear()
#--------------------------------------------------------------------------------------
    print("-="*20)
    resp = str(input("Deseja continuar? [ S | N ]: ")).upper().strip()
    if resp == "N":
        break
    
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

