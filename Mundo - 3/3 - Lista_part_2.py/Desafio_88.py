'''
Faça um programa que ajuda um jogador da mega sena a criar palpites. O programa
vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.

5 Q's

1 - Quais são os dados de entrada?

- Quantidade de jogos a ser gerado;
- Para cada jogo vamos gerar 6 números

2 - O que devo fazer com esses dados

- Vamos gerar 6 números para cada jogo definido pelo usuario

3 - Quais são as restrições do problema?

- Serão 6 números entre 1 e 60 para cada jogo.

4 - Qual é o resultado esperado?

- O usuario deverá informar quantos jogos deseja gerar;
- Para cada jogo gerado, serão sorteados 6 números diferentes entre 1 á 60;
- No final vamos exibir o resultado para o usuario;

5 - Qual a sequência de passos para alcançar o resultado?
from radon import randint
Numeros gerados: [[],[],[],[],[],[]]
While True
    n = input Quantos jogos quer gerar
    for c in range(0, n):
        gerados = randint(1,60)
'''
from random import randint
#Montagem dos jogos_______________________________________________________________
numeros_sorteados = []
dados_finais = []
while True:
    n = int(input("Quantos jogos você quer gerar: "))#Pergunta quantidade de jogos
    for c in range(n):
        for _ in range(6):
            sorteio_numeros = randint(0,60)
            numeros_sorteados.append(sorteio_numeros)
        dados_finais.append(numeros_sorteados[:])
        numeros_sorteados.clear()
#Exibição dos jogos_______________________________________________________________
    for i, jogo in enumerate(dados_finais, 1):
        print("-="*20)
        print(f"{i}°jogo: {jogo}") 
    dados_finais.clear()
#Verificação para continuar_______________________________________________________
    while True:
        print("-="*20)
        continuar = str(input("Deseja continuar [S|N]: ")).upper().strip()
        if continuar not in 'SN':
            continue
        elif continuar in 'SN':
            break
    if continuar in 'N':
        break
    