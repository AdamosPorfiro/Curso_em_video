'''
Desenvolva um programa que leia, nome, idade e sexo de quatro pessoas. No final do programa mostre:

- A média de idade do grupo;
- Qual é o nome do homem mais velho;
- E quantas mulheres tem menos de 20 anos;

'''
media = 0
mais_velho = 0
nome_mais_velho = " "
qtd_mulheres_menor_de_20 = 0
for c in range(1,5):
    print("="*15)
    nome = str(input("Nome: ")).strip().upper()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo | M | F |: ")).strip().upper()
    print("="*15)

    # Média
    media = media+idade

    # Nome do homem mais velho
    if sexo in "M":
        if idade > mais_velho:
            mais_velho = idade
            nome_mais_velho = nome
    #Quantas mulheres tem menos de 20 anos
    if sexo in "F":
        if idade < 20:
            qtd_mulheres_menor_de_20 += 1
print(f"A média de idade desse grupo é {media / 4}")
if mais_velho != 0:
    print(f"O homem mais velho tem {mais_velho} e o seu nome é: {nome_mais_velho.capitalize()}")
else:
    print("Não há homens nesse grupo")
print(f"Quantidade de mulheres com menos de 20 anos é: {qtd_mulheres_menor_de_20} mulheres")
