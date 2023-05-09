'''

===== Desafio 5 =====

Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

Metodo 5 Q's

1 - Quais são os dados de entrada?
-> input n1_inteiro.

2 - O que deve ser feito com esses dados?
-> Deve ler e mostrar na tela a sua tabuada.

3 - Existe alguma restrição nesse problema?
-> Apenas numeros inteiros.

4 - Qual o resultado esperado?
-> Exibir na tela a tabuada do dado digitado.

5 - Qual é a sequência de passos a ser feito para se alcançar o resultado esperado?
1 - input n1 
2 - print n1 * 1
3 - print n1 * 2...Tabuada completa

'''

print('=' * 23, 'Desafio 5','=' * 23,'\n' , ' ' * 16, 'Conversor de tabuada')
n1 = int(input('\nDigite um numero para ter a tabuada de 1 a 10 desse numero\n'))

print('\n1 x {} = {}'.format(n1, 1 * n1))
print('2 x {} = {}'.format(n1, 2 * n1))
print('3 x {} = {}'.format(n1, 3 * n1))
print('4 x {} = {}'.format(n1, 4 * n1))
print('5 x {} = {}'.format(n1, 5 * n1))
print('6 x {} = {}'.format(n1, 6 * n1))
print('7 x {} = {}'.format(n1, 7 * n1))
print('8 x {} = {}'.format(n1, 8 * n1))
print('9 x {} = {}'.format(n1, 9 * n1))
print('10 x {} = {}'.format(n1, 10 * n1))
print('=' * 29 + '=' * 29)