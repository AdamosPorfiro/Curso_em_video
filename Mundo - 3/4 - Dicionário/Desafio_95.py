"""
Aprimore o desafio 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

Jogador = dict()
Partidas = list()
Jogadores = list()

while True:
    Jogador["nome"] = str(input("Nome jogador: "))
#--------------------------------------------------------------------------------------
    while True:
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
    Jogador.clear()
#--------------------------------------------------------------------------------------
    print("-="*30)
    resp = str(input("Deseja continuar? [ S | N ]: ")).upper().strip()
    print("-="*30)
    if resp == "N":
        break

#--------------------------------------------------------------------------------------  
print("-"*50)
print(f"{"cod"}{"|":>4}{"nome":>6}{"|":>6}{"gols":>9}{"|":>4}{"total":>10}")
print("-"*50)
for indice,valor in enumerate(Jogadores):
    print(f"{indice}",end='')
    for v in valor.values():
        print(f"{str(v):>12}",end='')