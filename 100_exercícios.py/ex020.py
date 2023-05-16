'''
===== Exercício 20 =====

Um professor quer sortear um dos seus alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome do escolhido.

metodo dos 5 Q's

1 - Quais são os dados de entrada?
-> input nomes_de_alunos

2 - O que devo fazer com esses dados?
-> Usando a biblioteca radom e sua função choice vamos fazer com que o programa sorteie um dos nomes
para apagar o quadro.

3 - Quais são as restrições do programa?
-> Apenas nomes strings 

4 - Qual o resultado esperado?
-> Que o programa sorteie um nome de uma lista de alunos para apagar o quadro.

5 - Quais são os passos necessario para se alcançar o resultado?
1 - importar a biblioteca radom e função choice;
2 - Variavel com os nomes do alunos;
3 - print sorteando um dos nomes inseridos na variavel;

'''

from random import choice
li_nomes = [] # Declaração de uma lista vazia;
li_nomes.append("Adamos") #.append para armazenar elemento a lista;
li_nomes.append("Alesson")
li_nomes.append("Vilma")
li_nomes.append("Antônio")
li_nomes.append("Pâmela")
li_nomes.append("João")
li_nomes.append("Maria")
print(choice(li_nomes)) # Função choice vai sortear um dos nomes da lista e exibir na tela;