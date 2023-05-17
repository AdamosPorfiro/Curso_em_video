'''
===== Exercicio 16 =====
Crie um programa que leia um numero real qualquer pelo teclado e mostre na sua tela a sua porção inteira.
Ex.: Digite um numero: 6.127
O numero 6.127 tem a parte inteira 6

Resolva utilizando modulos para praticar.

metodo dos 5 Q's

1 - Quais são os dados de entrada?
R: importar a biblioteca math_trunc
   input numero_real.

2 - O que deve ser feito com esses dados?
R:: Deve exibir na tela apenas sua porção inteira.

3 - Quais são as restrições desse problema?
R: Deve utilizar modulos; Numeros reais(decimais).

4 - Qual é o resultado esperado?
R: Que o numero real digitado, seja convertido apenas a sua porção inteira, sem os decimais, pontos flutuantes.

5 - Quais são os passos para se alcançar o resultado?
R: 
1 - Iportar a biblioteca math_trunc
2 - input numero_real
3 - Usar uma função da biblioeca math para exibir na tela apenas a porção inteira do numero_real = trunc
4 - print numero_real e trunc(Que vai quebrar o numero, tirando os decimais)
'''

from math import trunc #Podemos tambem usar o floor, que vai arredondar o valor
print('\n' + '=' * 11, 'Coversor de numeros reais para inteiros', '=' * 12)
num = float(input('\nDigite um numero. Use ponto para separar os decimais Ex.: 6.127\nNumero:  '))
print('\nO numero escolhido foi {:.3f}.\nE sua porção inteira é {}.'.format(num,trunc(num)),'\n' + '=' * 64)
