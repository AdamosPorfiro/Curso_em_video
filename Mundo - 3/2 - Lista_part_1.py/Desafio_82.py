'''
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores impares digitados
respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''
numeros = []
pares = []
impares = []
while True:
    print("-="*15)
    n = int(input("Digite um número: "))
    numeros.append(n)
    print("-="*15)
    while True:
        continuar = str(input("Deseja continuar [S|N]: ")).strip().upper()
        if continuar not in 'SN':
            continue
        elif continuar in 'S':
            break
        elif continuar in 'N':
            break
    if continuar in 'N':
        break
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f"Lista de números informados: {numeros}")
print(f"Lista de números pares: {pares}")
print(f"Lista de números ímpares: {impares}")