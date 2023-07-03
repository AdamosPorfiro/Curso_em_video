'''
Crie uma tupla preennchida com os 20 primeiros colocados da tabela do campeonato brasileiro de
futebol, na ordem de colocação. Depois mostre:

A - Apenas os 5 primeiros colocados.
B - Os últimos 4 colocados da tabela.
C - Uma lista com os times em ordem alfabética.
D - Em que posição na tabela está o time da Chapecoense.

1 - Botafogo
2 - Grêmio
3 - Flamengo
4 - Pameiras
5 - Bragantino
6 - Fluminense
7 - São paulo
8 - Internacional
9 - Athletico - PR
10 - Atlético - MG
11 - Fortaleza
12 - Cruzeiro
13 - Cuiabá
14 - Santos
15 - Bahia
16 - Corinthians
17 - Goás
18 - Vasco da Gama
19 - América - MG
20 - Coritiba
'''

Tabela = ('Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Bragantino', 'Fluminense',
          'São Paulo', 'Internacional', 'Athlético - PR', 'Atlético - MG', 'Fortaleza',
          'Cruzeiro', 'Cuiabá', 'Santos', 'Bahia', 'Corinthians', 'Goiás',
          'Vasco da Gama', 'América - MG', 'Coritiba', 'Chapecoense')
print('5 PRIMEIROS COLOCADOS\n')

# A - Apenas os 5 primeiros colocados.
for indices, colocados in enumerate(Tabela):
    if indices <= 4:
        print(colocados)

# B - Os últimos 4 colocados da tabela
print('\n4 ULTIMOS COLOCADOS\n')
for indices, colocados in enumerate(Tabela):
    if indices >= 16 and indices <= 19:
        print(colocados)

# C - Uma lista com os times em ordem alfabética.
print('\nORDEM ALFABÈTICA\n\n',sorted(Tabela))

# D - Em que posição na tabela está o time da Chapecoense.
if colocados in 'Chapecoense':
    print('\nChapecoense está em:',indices+1,'° Posição')
else:
    print('\nNão está na tabela')
