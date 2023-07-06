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

Tabela = ('Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Bragantino', 'Fluminense',
          'São Paulo', 'Internacional', 'Athlético - PR', 'Atlético - MG', 'Fortaleza',
          'Cruzeiro', 'Cuiabá', 'Santos', 'Bahia', 'Corinthians', 'Goiás',
          'Vasco da Gama', 'América - MG', 'Coritiba')
# A - Apenas os 5 primeiros colocados da tabela:
print('5 Primeiros colocados\n{:=^25}'.format(''))
for indice, colocados in enumerate(Tabela):
    while indice < 5:
        print(colocados)
        break
# B - Os últimos 4 colocados da tabela.
print('{:=^25}\n\n4 Ultimos colocados\n{:=^25}'.format('',''))
for indice, colocados in enumerate(Tabela):
    while indice >= 16 and indice < 20:
        print(colocados)
        break
# C - Uma lista com os times em ordem alfabética.
print('{:=^25}\n\nOrdem Alfabética\n{:=^25}'.format('',''),'\n',sorted(Tabela),'\n{:=^25}'.format(''))

# D - Em que posição na tabela está o time da Chapecoense.

if colocados in 'Chapecoense':
    print('\n',indice+1,'° Posição')
else:
    print('\nChapecoense não está mais na tabela')
'''
Tabela = ('Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Bragantino', 'Fluminense',
          'São Paulo', 'Internacional', 'Athlético - PR', 'Atlético - MG', 'Fortaleza',
          'Cruzeiro', 'Cuiabá', 'Santos', 'Bahia', 'Corinthians', 'Goiás',
          'Vasco da Gama', 'América - MG', 'Coritiba','Chapecoense')
#  A - Apenas os 5 primeiros colocados.
print('='*80)
print(f'Os 5 primeiros colocados: {Tabela[0:5]}')
print('='*80)
# B - Os últimos 4 colocados da tabela.
print(f'Os 4 últimos colocados: {Tabela[-4:]}')
print('='*80)
# C - Uma lista com os times em ordem alfabética.
print(f'Orden alfabética: {sorted(Tabela)}')
print('='*80)
# D - Em que posição na tabela está o time da Chapecoense.
print(f'O Chapecoense está na posição {Tabela.index("Chapecoense")+1}')