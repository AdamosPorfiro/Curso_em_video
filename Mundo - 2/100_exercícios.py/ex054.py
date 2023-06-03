'''
Crie um programa que leia o ano de nascimento de 7 pessoas. No final diga quantas pessoas
ainda não atingiram maioridade e quantas já são maiores.

Ex: 18 anos

Quais são os dados de entrada?
input ano_nascimento

O que devo fazer com esses dados?
Calcular a idade de cada um e armazena-los em um lista em seguida compara-lás para descobrir quem é maioro ou menor

Qual a restrição desse problema?
Maioridade = 18+ anos;
Menores = 17- anos;

Qual é o resultado esperado?
Ler as 7 datas, calcular e exibir quantas pessoas ainda não atingiram a maioridade e quantas são menores

Quais são os passos para se alcançar o resultado esperado?
    1 import datetime / date 
    2 ano[]
    3 for input ano_nascimento
    4 idade[]
    5 data = date.today().year
    5 for i in ano:
        i = i -= data
        i.append(idade)
    6 maior = []
    7 menor = []
    8 for s in idade:
    9   if s>=18:
            s.append(maior)
    10  else:
            s.append(menor)
    11 print Possui {} maior e {} menores. format len(maior), len(menor)      


lista = [] # Cria uma lista vazia;
for idade in range(7): # Repete o input 7x e armazena dentro de lista;
    idade = str(input('Qual a sua idade?\nIdade: ')).strip()
    lista.append(int(idade))
maior = [] # Crio duas listas vazia para armazenar pessoas maiores de idade e menores de idade;
menor = []
for item in lista: # Crio outro for para passar na primeira lista que criamos
    if item>=18: # Se o elemento que for passar pelo for, for maior que ou igual a 18 ele vai inserir esse lemento na lista maior
        maior.append(item)
    elif item<18: # Caso seja menor que 18 ele vai inserir o elemento na lista menor
        menor.append(item)
print('\nPossui {} maiores de idade\nPossui {} menores de idade'.format(len(maior), len(menor))) # Usamos len para ler a quantidade de elemento dentro de cada lista e exibimos;
'''
from datetime import date 
Ano = []
maior = []
menor = []
ano_a = date.today().year
for item in range(1, 8):
    i = int(input('informe o {}° Ano de nascimento: '.format(item)))
    Ano.append(i)
for item in Ano:
    Ano = ano_a - item
    if Ano>=18:
        maior.append(Ano)
    else:
        menor.append(Ano)
print('\nQuantidade de pessoas maiores de idade: {}\nQuantidade de pessoas menores de idade: {}'.format(len(maior), len(menor)))

        


