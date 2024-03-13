'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:

A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os numeros pares.
'''
print("-="*20) 
print("{:>25}".format(" Desafio 75 ")) 
print("-="*20) 
valor_9 = posição = numero_tres = contador_de_pares = 0
valor_guardado  = [] #Crio uma lista para armazenar os valores digitados através da função .append
numeros_pares = []

for c in range(1,5):
    valor = int(input(f"Informe {c}° valor: "))
    if valor == 9:
        valor_9 += 1
    valor_guardado.append(valor) #Usamos a função append para guardar valor em valor_guardado
valor_guardado = tuple(valor_guardado)


for pos, numero in enumerate(valor_guardado):
    if numero_tres == 3:
        break
    elif numero == 3:
        posição = pos+1
        numero_tres = numero
    if numero % 2 == 0:
        contador_de_pares += 1
        numeros_pares.append(numero)
if valor_9 > 0:
    print(f"O valor 9 apareçe {valor_9} vezes")
else:
    print("Não foram digitados valores 9")
if posição > 0:
    print(f"A posição do 1° numero três é: {posição}° Posição")
else:
    print("Não foi digitado valores 3")
if contador_de_pares > 0:
    print(f"Numeros pares digitados são: {numeros_pares}")
else:
    print("Não foram digitados valores pares")
print("-="*20)
