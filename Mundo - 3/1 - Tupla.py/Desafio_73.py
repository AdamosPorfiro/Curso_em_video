'''
Crie uma tupla preennchida com os 20 primeiros colocados da tabela do campeonato brasileiro de
futebol, na ordem de colocação. Depois mostre:

A - Apenas os 5 primeiros colocados.
B - Os últimos 4 colocados da tabela.
C - Uma lista com os times em ordem alfabética.
D - Em que posição na tabela está o time da Chapecoense.

'''

tabela_times = (
    'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia','Botafogo', 'Cortinthians',
    'Criciúma', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional',
    'Juventude', 'Palmeiras', 'Bragantino', 'São paulo', 'Vasco da gama', 'Chapecoense'
)
print(f"Os 5 primeiros colocados\n")
for pos, time in enumerate(tabela_times[0:5]):
    print(f"{pos+1}° {time}")
print("-="*15)
print("Of últimos 4 colocados\n")
for pos, time in enumerate(tabela_times[16:21]):
    print(f"{pos+1}° {time}")
print("-="*15)
print("Tabela em ordem alfabética\n")
print(sorted(tabela_times))
print("-="*15)
print("Chapecoense está na posição\n")
for pos,time in enumerate(tabela_times):
    if time in 'Chapecoense':
        print(f"{pos+1}° {time}")
print("-="*15)

    