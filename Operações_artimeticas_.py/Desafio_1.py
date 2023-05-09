'''
===== Desafio 1 =====

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
print ('=' * 6,'Desafio 1','=' * 6,'\n')
n1 = int(input('Digite um numero inteiro para saber o seu sucessor e antecessor\n'))
print ('\nO sucessor de {} é: {:=^15}'.format(n1, n1 + 1),'\nE o antecessor de {} é: {:=^15}'.format(n1, n1 - 1))