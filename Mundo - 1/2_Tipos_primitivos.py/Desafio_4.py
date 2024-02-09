#Crie um programa que leia dois numeros e mostre a soma deles

print ('===== Desafio 4 =====')
n1 = (input('Digite algo: '))
print("\nTrue = Sim / False = Não\n")
print("O valor digitado e numerico? ", n1.isnumeric())
print("O valor digitado e uma string? ", n1.isalpha())
print("O valor digitado e um numero? ", n1.isalnum())
print("O valor digitado esta em maiusculo? ", n1.isupper())
print("O valor digitado esta em minusculo? ", n1.islower())
print("O valor digitado é imprimivel ? ", n1.isprintable())
"""resultado = int(n1) + int(n2)
print ('A soma de {} + {} = {}' .format (n1, n2, resultado))"""