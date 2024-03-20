'''
Crie um programa onde o usuario podera digitar sete valores númericos e
cadastre-os em uma lista única que mantenha separados os valores pares e
ímpares. No final mostre os valores pares e ímpares em ordem crescente.
'''
lista_de_numeros = []
pares = []
ímpares = []
for c in range (0,7):
    lista_de_numeros.append(int(input("Digite um valor: ")))
    for c in lista_de_numeros:
        if c % 2 == 0:
            pares.append(c)
        else:
            ímpares.append(c)
    lista_de_numeros.clear()
print(f"Pares: {sorted(pares)}\nImpares: {sorted(ímpares)}")