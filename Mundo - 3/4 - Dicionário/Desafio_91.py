"""
Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses
resultados em um dicionario. No final coloque esse dicionário em ordem
sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
resultado_inicial = dict()
resultado_oficial = list()
outra_lista = list()
maior = 0

#Programa que guarda o resultado em um dicionario e gera uma copia para um lista organizada
for c in range(4):
    print(f"{c+1}°Jogador...rolando dado")
    resultado_inicial["numero"] = randint(1,6) #Gerar os numeros e armazenar em um dicionario
    print(f"{resultado_inicial.values()}")
    sleep(0.7)
    resultado_oficial.append(resultado_inicial.copy())
resultado_inicial.clear()

for r in resultado_oficial: #Entro dentro da lista que existe os dicionarios
    for k,v in r.items():
        if v > maior:
            maior = v
        outra_lista.append(v)
print(f"{sorted(outra_lista)}")
print(f"O vencedor jogou: {maior}")

        
