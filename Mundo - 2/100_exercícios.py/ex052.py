"""
Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.

Analise:

O que é um numero primo?
R: É um numero primo aquele que é maior que 1 e possui 2 divisores, sendo eles: 1 e ele mesmo, ou seja,
um numero primo é quando o numero é divisivel de forma exata por 1 e por ele mesmo.

Podemos identifica-lo usando os seguintes termos:
1 - Verificando se o numero é maior que 1;
2 - Verifique se o numero é divisivel por um numero inteiro maior que 1 e menor que ele mesmo;
           - Se houver um numero divisor maior que 1 e menor que ele mesmo, então, o numero não é primo;
           - Se o numero for divisivel apenas por 1 e ele mesmo, então, o numero é primo;

Quais são os dados de entrada?
input numero

O que devo fazer com esses dados?
Exibir na tela se ele é um numero primo ou não

Quais são as restrições desse problema?
Apenas numero primos

Qual é o resultado esperado?
Exibir na tela se o numero informado é primo ou não.

Quais são os passos necessarios para se chegar ao resultado esperado?
input numero
if > 1
    for c in range(2, numero)
        if numero%c == 0:
        Não é primo
        para aqui
    else 
        É primo
else:
    print Não é primo

"""

n = int(input('Informe um numero: '))
if n > 1:
    for c in range(2,n):
        if n%c == 0:
            print('{} Não é primo'.format(n))
            break
    else:
        print('{} é primo'.format(n))
else:
    print('{} é primo'.format(n))