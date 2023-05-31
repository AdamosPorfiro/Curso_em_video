'''
Crie um programa que leia o ano de nascimento de 7 pessoas. No final diga quantas pessoas
ainda não atingiram maioridade e quantas já são maiores.

Ex: 18 anos

Analise: 
- Usamos um for para repetir o input 7 vezes;
- Podemos montar uma lista;
- Usar função FOR para passar por cada elemento da lista e verificar quem atingiu a maioridade ou não;
- E no fim usar uma condição para exibir quantas são maiores e quantas são menores

Quais são os dados de entrada?
input idade 7x

O que devo fazer com esses dados?
Armazena-los em uma lista para verificar em seguida quem atingiu a maioridade ou não;

Qual a restrição desse problema?
Maioridade = 18+ anos;
Menores = 17- anos;

Qual é o resultado esperado?
Ler as 7 idades e exibir quantas pessoas ainda não atingiram a maioridade e quantas são menores

Quais são os passos para se alcançar o resultado esperado?
    1 lista[]
    2 for 7 input idade
    3   idade = lista
    4 for item in lista:
    5   if item >= 18:
            maior = []
            item = maior
        elif(if) item <= 17:    
            menor = []
            item = menor
    6 for qtd_maior in maior:
        if maior:
            print(qtd_maior)
    7 for qtd_menor in menor:
        if menor:
            print(qtd_menor)
'''

lista = []
for idade in range(7):
    idade = int(input('Qual a sua idade?\nIdade: '))
    lista.append(idade)
maior = []
menor = []
for item in lista:
    if item>=18:
        maior.append(item)
    elif item<18:
        menor.append(item)
print('\nPossui {} maiores')

'''
r_maior = 0
r_menor = 0
for qtd_maior in maior:
    r_maior = r_maior+qtd_maior
for qtd_menor in menor:
    r_menor = r_menor+qtd_menor
print('\nPossuem {} maiores de idade\nPossuem {} menores de idade'.format(r_maior,r_menor))
'''