"""
Aprimore o desafio 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

Jogador = dict()
Partidas = list()
Jogadores = list()

while True:
    Jogador.clear()
    Jogador["nome"] = str(input("Nome jogador: "))
#--------------------------------------------------------------------------------------
    while True:
        Partidas.clear()
        tot = str(input(f"Quantas partidas o jogador {Jogador["nome"]} jogou? "))
        if tot.isdigit():
            tot = int(tot)
            break
#--------------------------------------------------------------------------------------
    for c in range(0, tot):
        while True:
            Gols = (str(input(f"Quantos gols na partida {c+1}°? ")))
            if Gols.isdigit():
                Gols = int(Gols)
                Partidas.append(Gols)
                break
#--------------------------------------------------------------------------------------
    Jogador["Gols"] = Partidas[:]
    Jogador["Total"]= sum(Partidas)
    Jogadores.append(Jogador.copy())
#--------------------------------------------------------------------------------------
    while True:
        print("-="*30)
        resp = str(input("Deseja continuar? [ S | N ]: ")).upper().strip()
        print("-="*30)
        if resp not in 'SN':
            continue
        elif resp in 'SN':
            break
    if resp == 'N':
        break
#--------------------------------------------------------------------------------------  
print("-"*50)
print(f"{"cod":>4}{"|":>2}{"nome":>6}{"|":>4}{"gols":>7}{"|":>4}{"total":>10}")
print("-"*50)

for indice,valor in enumerate(Jogadores):
    print(f"{indice:>4}  ",end='')
    for v in valor.values():
        print(f"{str(v):<15}",end='')
    print()
print("-"*50)
