'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final mostre os 10 primeiros termos  dessa progressão.

O que é o primeiro termo e a razão de uma PA
R:. É uma sequencia de termos onde a diferença entre um termo e o seu anterior é sempre constante.
Para escrever essa progressão precisamos da "primeiro termo" e da sua "razão" 

Termo: 6 <-
Razão: 3

Primeiro termo é: 6
Segundo termo é: 6+3 = 9, logo segundo termo é 9
terceiro termo é: 12... 
'''
print("=-"*28)
print("{:>32}".format(" Desafio 51 "))
print("=-"*28)
termo = int(input("Informe o termo: "))
razao = int(input("Informe a razão: "))
print("\n")
#print(f"\nOs 10 primeiro são:\n 1° termo {termo}")
for c in range(1,11):
    print(f"{termo}",end=' → ')
    termo += razao
    #print(f"{c:2}° termo: {termo}")
print("Acabou"+"\n"+"=-"*28)

