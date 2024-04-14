"""
Crie um programa que gerencie o aproveitamento de um jogador
de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols
feitos em cada partida. No final, tudo isso será guardado em um
dicionário incluindo o total de gols feitos durante o campeonato
"""

dados_jogador = dict()
dados_finais_jogador = list()
quantidade_de_gols = 0

dados_jogador["nome"] = str(input("Nome: "))
dados_jogador["Numero_partidas"] = int(input("Quantidade de partidas: "))
dados_finais_jogador.append(dados_jogador.copy())
dados_jogador.clear()

for c in range(dados_finais_jogador[0]["Numero_partidas"]):
    dados_jogador[f"qtd_gols_partida"] = int(input(f"Quantos gols foram feitos na {c+1}° partida: "))
    dados_finais_jogador.append(dados_jogador.copy())
    dados_jogador.clear()

for r in dados_finais_jogador:
    for k, v in r.items():
        if k == "qtd_gols_partida":
            quantidade_de_gols += v
dados_jogador["total_de_gols"] = quantidade_de_gols
dados_finais_jogador.append(dados_jogador.copy())
