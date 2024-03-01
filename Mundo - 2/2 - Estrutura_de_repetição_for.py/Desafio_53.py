'''
Crie um programa que leia um frase qualquer e diga se ela é um palindromo. Desconsiderando os espaços e acentos.

Palindromo são palavras ou frases que podem ser lidar do começo pro fim ou do fim pro começo;

Ex: Apos a sopa, A sacada da casa, A torre da derrota, O lobo ama o bolo, Anotaram a data da maratona.

'''
print("-="*30)
print("{:>35}".format(" Desafio 53 "))
print("-="*30)
frase = str(input("Digite um PALINDROMO: ")).strip().lower()

frase = ''.join(frase.split()) # Juntar a frase, para facilitar a comparação no final do programa

palindromo = '' # Armazena a frase escrita ao contrario para comparar no final do programa

for c in range(len(frase[:-1])+1): # Lê as posições da frase de trás para frente
    palindromo = frase[c]+palindromo # Armazena cada letra na dentro da variavel palindromo

# Compara as frases
if frase == palindromo:
    print(f"A frase {frase.capitalize()} é {palindromo.capitalize()} é um palindromo")
else:
    print(f"A frase {frase.capitalize()} é {palindromo.capitalize()} não é um palindromo")
print("-="*30)




