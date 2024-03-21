'''
Crie um programa onde o usuario podera digitar sete valores númericos e
cadastre-os em uma lista única que mantenha separados os valores pares e
ímpares. No final mostre os valores pares e ímpares em ordem crescente.
'''

pares_impares = [[], []] #Criar uma lista única com sublistas que são listas dentro de listas.
for c in range (7):
    numero = int(input("Digite um valor: "))
    if numero % 2 == 0:
        pares_impares[0].append(numero)
    else:
        pares_impares[1].append(numero)
#----------------------------------------------------
print("-="*10)
print(f"Números pares são: {sorted(pares_impares[0])}")
print(f"Números ímpares são: {sorted(pares_impares[1])}")
print("-="*10)