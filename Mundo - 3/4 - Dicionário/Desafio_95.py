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
print("cod   ",end='')
for i in Jogador.keys():
    print(f"{i:<15}", end='')
print()
print("-"*50)
#--------------------------------------------------------------------------------------  
for indice,valor in enumerate(Jogadores):
    print(f"{indice:>4}  ",end='')
    for v in valor.values():
        print(f"{str(v):<15}",end='')
    print()
print("-"*50)
#--------------------------------------------------------------------------------------  
while True:
    Escolha = int(input("Mostrar dados de qual jogador? [999] para sair: "))
    if Escolha == 999:
        break
    if Escolha > len(Jogadores):
        print(f"Não existe jogador com o código {Escolha}")
    else:
        print(f"Levantamento do jogador {Jogadores[Escolha]["nome"]}:")
        for indice, valor in enumerate([Jogadores[Escolha]['Gols']]):
            print(f"       No jogo {indice+1} fez {valor} Gols")
            print("-"*50)
print("VOLTE SEMPRE")
        
