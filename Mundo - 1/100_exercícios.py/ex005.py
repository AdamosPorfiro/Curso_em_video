'''
===== Exercicio 5 =====

Faça um programa que leita um numero inteiro e mostre o seu sucessor e o seu antecessor.

Metodo 5 Q's

1 - Quais são os dados de entrada?
    -> inpu n_inteiro.

2 - O que devo fazer com esses dados?
    -> Mostrar o seu sucessor e o seu antecessor.

3 - Quais são as restrições do programa?
    -> Apenas numeros inteiros.

4 - Qual o resultado esperado?
    -> Ler um numero inteiro e mostrar o seu sucessor e o antecessor.

4 - Qual a sequência de passos a ser feita para chegar ao resultado?

===== Pseudocódigo =====
    -> input n_inteiro
    -> s = n_inteiro + 1
    -> a = n_inteiro - 1
    -> print numero sucessor de n_inteiro é s e antecessor é a

'''

print ('=' * 25, 'Exercicio 5' , '=' * 25)
n1 = int(input('\nDigite um numero inteiro para exibir o seu sucessor e antecessor\nnumero:'))
print('\nO sucessor do número {}{}{} é: {}{}{}\nO antecessor do número  {}{}{} é: {}{}{}'.format('\033[1;30;41m',n1,'\033[m', '\033[32m', (n1 + 1),'\033[m','\033[1;30;41m', n1,'\033[m','\033[32m', (n1 - 1),'\033[m'),'\n'+'=' * 63)