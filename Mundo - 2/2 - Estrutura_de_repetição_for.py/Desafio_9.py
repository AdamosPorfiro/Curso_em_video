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
