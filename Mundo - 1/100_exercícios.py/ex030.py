'''
Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR.

1 - Quais são os dados de entrada?
- input numero_inteiro

2 - O que devo fazer com esses dados?
- Ler e exibir se o numero é impar ou par;

3 - Quais são as restrições desse problema?
- Apenas numero inteiro;
- Exibir se é impar ou par.

4 - Qual é o resultado esperado?
- Exibir se o numero é impar ou par.

5 - Quais são os passos necessarios para se alcançar o resultado esperado?
#1 input numero_inteiro
#2 variavel1 = numero_inteiro % 2
#3 if variavel1 == 0:
        print O numero_inteiro é PAR
    else
        print O numero_inteiro é IMPAR
'''
print('\n'+'=' * 28,'\n','\nCALCULADORA DE IMPAR OU PAR\n')
n = int(input('Informe um numero inteiro\nNumero: '))
r = n % 2
if r == 0:
    print('O numero {} é PAR.'.format(n))
else:
    print('O numero {} é IMPAR'.format(n))
print('=' * 28)