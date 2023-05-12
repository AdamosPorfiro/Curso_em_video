'''
===== Exercício 2 =====

Crie um programa que leia um numero e mostre o seu dobro, triplo e a raiz quadrada.

Metodo dos 5Q's

1 - Quais são os dados de entrada?
 -> input numero.

2 - O que devo fazer com esses dados?
 -> Deve ler um numero e exibir o dobro, triplo e a raiz quadrada desse numero.

3 - Quais são as restrições desse problema?
 -> Nenhuma

4 - Qual é o resultado esperado?
  -> Exibir o dobro, triplo e a raiz quadrada do dado de entrada

5 - Quais são os passos para se alcançar o resultado esperado?
#1 - input numero
#2 - print O dobro do numero é: numero * 2 O triplo do numero é: numero * 3 A raiz quadrada do numero é: numero ** 2

'''

print('=' * 25, 'Exercicio 6', '=' * 26)
n1 = int(input('\nDigite um número para calcular o dobro, triplo e a raiz quadrada\nNumero: '))
print ('\nO dobro de {} = {}\nO triplo de {} = {}\nA raiz quadrada de {} = {}'.format(n1,(n1 * 2), n1, (n1 * 3), n1, (n1 * 1/2)),'\n'+'=' * 64)