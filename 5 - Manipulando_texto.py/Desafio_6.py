'''
Faça um programa que leia um nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

Ex.: Ana Maria de Souza;
Primeiro: Ana;
Ultimo: Souza.

Analise critica: Vamos usar função split para dividir as palavras e depois acessa-lás por meio de indexação.

1 - Quais são os dados de entrada?
input nome_completo;
nome_completo.split();
index_1 = nome_completo[0] indice 0 indica a primeira palavra;
index_2 = nome_completo[-1] indice -1 é a ultima palavra;

2 - O que devo fazer com esses dados?
Exibir na tela o primeiro e o ultimo nome separadamente

3 - Quais são as restrições desse problema?
Deve exibir o primeiro e o ultimo nome

4 - Qual o resultado esperado?
Exibir na tela o primeiro e o segundo nome

5 - Quais os passos para se alcançar o resultado?
#1 input nome_completo
#2 Variavel_1=nome_completo.split()
#3 Variavel_2 = Variavel_1[0] 
#4 Variavel_3 = Variavel_1[-1]
#5 Print da Variavel_2 e Variavel_3
'''

nome = str(input('Nome completo: '))
separar = nome.split()
n1 = separar[0]
n2 = separar[-1] # -1 Representa o ultimo elemento da lista
print('Primeiro nome: {}\nUltimo nome: {}'.format(n1,n2))