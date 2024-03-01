'''
Desenvolva um programa que leia 6 numeros inteiros, e mostre a soma apenas daqueles que forem pares, se o valor digitado for
impar desconsidere-o

'''

soma = 0
cont = 0
for c in range(1,7):
    n = int(input(f"Informe {c}° número inteiro: "))
    if n % 2 == 0:
        soma += n
        cont += 1
if soma != 0:
    print(f"\nVocê informou {cont} pares.\nA soma desses números é {soma}")
else:
    print("\nNão exite número pares para somá-los")