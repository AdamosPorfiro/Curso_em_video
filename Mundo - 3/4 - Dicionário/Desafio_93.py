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
for c in range(dados_jogador["Numero_partidas"]):
    dados_jogador["qtd_gols_partida"] = int(input(f"Quantos gols foram feitos na {c+1}° partida: "))
    dados_finais_jogador.append(dados_jogador["qtd_gols_partida"])
print(f"{dados_finais_jogador}")