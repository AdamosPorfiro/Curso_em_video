'''
===== Exercicio 21 =====

O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

1 - Quais são os dados de entrada?
-> import biblioteca random a função shuflle
-> input grupo_1
-> input grupo_2
-> input grupo_3
-> input grupo_4

2 - O que devo fazer com esses dados?
-> Vai sortear a ordem de apresentação de quatro grupos de alunos e mostrar a ordem sorteada

3 - Quais são as restrições desse problema?
-> Iremos sortear uma ordem de elementos usando biblioteca shuffle

4 - Qual o resultado esperado?
-> Exibir na tela a ordem sorteada

5 - Quais são os passos para se alcançar o resultado?
-> Importar a biblioteca choice e função shuffle
-> Montar uma lista com os 4 grupos
-> Print uma ordem aleatoria dos grupos usando a função shuffle

'''


from random import choice, shuffle
grupos = []
grupos.append("grupo 1")
grupos.append("grupo 2")
grupos.append("grupo 3")
grupos.append("grupo 4")
shuffle(grupos)
print(grupos)
