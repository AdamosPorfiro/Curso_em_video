"""
Desafio 26

Faça um programa que leia uma frase pelo teclado e mostre:

- Quantas vezes apareçe a letra "A"
- Em que posição ela aparece a primeira vez
- Em que posição ela apareçe a ultima vez
"""
print("{:=^50}".format(" Desafio 26 "))
frase = str(input("Digite um frase: ")).upper()
frase = ''.join(frase.split())
print("A letra 'A' apareçe {} vezes".format(frase.count("A")))
print("A letra 'A' apareçe a 1° vez na posição {}".format(frase.find("A")+1))
print("A letra 'A' apareçe uma ultima vez na posição {}".format(frase.rfind("A")+1))
print("{:=^50}".format(""))