'''
Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior;
- O segundo valor é o maior;
- Não existe valor maior, os dois são iguais;

'''
print("-="*20)
print("{:>30}".format("Comparando dois numeros"))
print("-="*20)
n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))

if n1 > n2:
    print("O primeiro valor é maior")
elif n2 > n1:
    print("O segundo valor é maior")
else:
    print("Não existe valor maior, os dois são iguais")
print("="*40)
