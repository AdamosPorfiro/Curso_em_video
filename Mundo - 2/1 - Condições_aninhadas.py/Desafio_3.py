'''
Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior;
- O segundo valor é o maior;
- Não existe valor maior, os dois são iguais;

1 - Quais são os dados de entrada?
- input n1
- input n2

2 - O que devo fazer com esses dados?
- Comparar eles e exibir na tela:
    O primeiro valor é o maior; (ou menor)
    O segundo valor é o maior; (ou menor)
    Não existe valor maior, os dois são iguais;

3 - Quais são as restrições do problema?
- numeros inteiros;
- Quem é o maior e quem é o menor ou se são iguais;
    
4 - Qual é o resultado esperado?
- Comparar os numeros e indicar se o primeiro é o maior ou o segundo ou se são iguais;

5 - Quais são os passos necessarios para se alcançar o resultado?
1 -> input n1 
2 -> input n2
3 -> if n1 > n2:
        print O primeiro valor é o maior 
        print O segundo valor é o menor
        print Valores não são iguais sendo que temos: {} e {}
4 -> elif n2 > n1:
        print O primeiro valor é o menor 
        print O segundo valor é o maior
        print Valores não são iguais sendo que temos: {} e {}
5 -> else:
        print Os valores são iguais sendo que temos: {} e {}


'''

#Importando biblioteca time, função sleep;
from time import sleep
print('\n'+'-=-' * 3,'Comparando numeros','-=-'*3)
#Input para receber valores e armazena-los na variavel n1, n2;
n1 = int(input('\nInsira um valor inteiro\nValor 1: '))
n2 = int(input('\nInsira um valor inteiro\nValor 2: '))
#Time de analise
print('\033[31m','\nAnalisando os valores...\n','\033[m')
sleep(1)
# Condição 1:
if n1>n2:
    print('O valor 1 é o','\033[32m''maior''\033[m')
# Condição 2:
elif n2>n1:
    print('O valor 2 é o', '\033[32m''maior''\033[m')
# Condição 3:
else:
    print('Ambos os valores são iguais\n')
print('\n'+'-=-'*12)