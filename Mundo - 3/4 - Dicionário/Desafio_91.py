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
maior_1 = maior_2 = vencedor = 0

#Programa que guarda o resultado em um dicionario e gera uma copia para um lista organizada
for c in range(4):
    print("="*25)
    print(f"{c+1}°Jogador...rolando dado")
    resultado_inicial["numero"] = randint(1,6) #Gerar os numeros e armazenar em um dicionario
    if resultado_inicial["numero"] > maior_1:
        maior_1 = c
    sleep(0.7)
    print(f"Caiu: {resultado_inicial["numero"]}")
    sleep(1)
    
    resultado_oficial.append(resultado_inicial.copy())
resultado_inicial.clear()

print("="*25)
for r in resultado_oficial: #Entro dentro da lista que existe os dicionarios
    for k,v in r.items():
        if v > maior_2:
            maior_2 = v
        outra_lista.append(v)

print(resultado_oficial)
print(f"{sorted(outra_lista)}")
print(f"O vencedor foi o {maior_1}° jogador que tirou: {maior_2}")

        
