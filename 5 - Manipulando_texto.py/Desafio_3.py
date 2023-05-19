"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

Metodo dos 5Q's

1 - Quais são os dados de entrada?
-> input cidade

2 - Oque devo fazer com esses dados?
-> Diga se ela começa ou não com o nome "Santo".

3 - Quais são as restrições desse problema?
-> Apenas cidades;
-> Se começa com o nome santo ou não.

4 - Qual o resultado esperado?
-> Que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

5 - Quais são os passos para se alcançar o resultado esperado?
1 - input cidade
2 - Variavel1 = cidade.lower()
2 - print cidade in santo
"""
'''
cidade = str(input("Digite o nome de uma cidade:\nCidade: "))
p = cidade.lower()
if('santo' in p):
    print('Sim, possui santo no nome!')
else:
    print('Não, possui santo no nome!')
'''
c = str(input('Nome da cidade: ')).strip()
m = c.lower()
print('\nAnalisando o nome da cidade...\nPossui santo no nome: {}'.format("santo" in m))