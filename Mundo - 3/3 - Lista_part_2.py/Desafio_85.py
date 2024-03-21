'''
Crie um programa onde o usuario podera digitar sete valores númericos e
cadastre-os em uma lista única que mantenha separados os valores pares e
ímpares. No final mostre os valores pares e ímpares em ordem crescente.
'''
lista_de_numeros = []
pares_impares = []
for c in range (0,7):
    lista_de_numeros.append(int(input("Digite um valor: ")))
    pares_impares.append(lista_de_numeros[:])
    lista_de_numeros.clear()
print(pares_impares)
    
#print(f"Pares: {sorted(pares_impares)}\nImpares: {sorted(pares_impares)}")