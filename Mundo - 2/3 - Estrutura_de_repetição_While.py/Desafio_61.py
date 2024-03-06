'''
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando WHILE

T = termo | R = tazão

Ex: T = 5 R = 2
PA = T+R
5 > 7 > 9 > 11 > 13 > 15 > 17 > 19 > 21 > 23
'''
print("-="*20)
print("{:>25}".format(" Desafio 61 "))
print("-="*20)
termo = int(input("Informe o termo: "))
razão = int(input("Informe a razão: "))
cont = 0
pa = termo
while cont < 10:
    print(f"{pa}", end=' ⮕ ')
    cont += 1
    pa += razão
print("Acabou")