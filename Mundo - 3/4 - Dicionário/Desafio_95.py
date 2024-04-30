"""
Aprimore o desafio 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

dados_jogador = dict()
dados_finais_jogador = list()
quantidade_de_gols = 0

while True:
    dados_jogador["nome"] = str(input("Nome: "))
    dados_jogador["Numero_partidas"] = int(input("Quantidade de partidas: "))
    dados_finais_jogador.append(dados_jogador.copy())
    dados_jogador.clear()

    resp = str(input("Continuar? [S/N]: ")).upper().strip()
    if resp == "N":
        break

for indice,valor in enumerate(dados_finais_jogador):
    dados_jogador[f""]
    print(f"{dados_finais_jogador[indice]["Numero_partidas"]}")
"""
    for c in range(dados_finais_jogador[0]["Numero_partidas"]):
        dados_jogador[f"qtd_gols_partida"] = int(input(f"Quantos gols foram feitos na {c+1}° partida: "))
        dados_finais_jogador.append(dados_jogador.copy())
        dados_jogador.clear()

    resp = str(input("Continuar? [S/N]: ")).upper().strip()
    if resp == "N":
        break

for r in dados_finais_jogador:
    for k, v in r.items():
        if k == "qtd_gols_partida":
            quantidade_de_gols += v
dados_jogador["total_de_gols"] = quantidade_de_gols
dados_finais_jogador.append(dados_jogador.copy())
dados_jogador.clear()
print("="*30)
print("Dados do jogador")
print("="*30)
for r in dados_finais_jogador:
    for k,v in r.items():
        if k == "nome":
            print(f"Nome: {v}")
        if k == "Numero_partidas":
            print(f"Total de partidas jogadas: {v}")

for c, r in enumerate(dados_finais_jogador[1:3]):
        for k,v in r.items():
            if k == "qtd_gols_partida":
                print(f"Quantidade de gols da {c+1}° partida: {v}")
print(f"Total de gols: {dados_finais_jogador[3]["total_de_gols"]}")
"""