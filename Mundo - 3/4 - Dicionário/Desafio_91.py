"""
Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses
resultados em um dicionario. No final coloque esse dicionário em ordem
sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
resultado_inicial = dict()
resultado_oficial = list()
outra_lista = list()

#Programa que guarda o resultado em um dicionario e gera uma copia para um lista organizada
for c in range(4):
    resultado_inicial["numero"] = randint(1,6)
    resultado_oficial.append(resultado_inicial.copy())
resultado_inicial.clear()

for r in resultado_oficial:
    for k,v in r.items():
        outra_lista.append(v)
        resultado_inicial[k] = outra_lista
        
print(f"{outra_lista}")

        
