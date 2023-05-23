'''

Escreva um programa que leia um numero inteiro qualquer e peça para o usuario qual será a base
de conversão:

1 - para binário;
2 - para octal;
3 - para hexadecimal;

Para realizar essas conversões usamos as funções:

bin() = binario | oct() = octal | hex() = hexadecimal;

1 - Quais são os dados de entrada?
- input numero;
- input conversão;

2 - O que devo fazer com esses dados?
- Converter para uma base conforme a escolha do usuario: binário, octal, hexadecimal;

3 - Quais as restrições desse problema?
- Numeros inteiro

4 - Qual o resultado esperado?
- Converter o numero digitado pelo usuario para a base de converção que ele escolher, sendo possivel converter para:
-Binário;
-Octal;
-Hexadecimal;

5 - Quais são os passos necessarios para se alcançar o resultado?
1 - input numero;
2 - input conversão;
3 - if input conversão == 1:
        print(O numero digitado convertido para binario bin(numero))
    if input conversão == 2:
        print(O numero digitado convertido para octal oct(numero))
    else:
        print(O numero digitado convertido para hexadecimal(numero))
'''
print('\nConversor de base binário, octal, hexadecimal')
n = int(input('\nInforme um numero inteiro\nNumero: '))
c = int(input('\n1 - Binário | 2 - Octal | 3 - Hexadecimal\nEscolha: '))
if c == 1:
    print('\nO numero convertido para binario fica assim: {}{}{}'.format('\033[32m',bin(n),'\033[m'))
elif c == 2:
    print('\nO numero convertido para octal fica assim: {}{}{}'.format('\033[32m', oct(n),'\033[m'))
else:
    print('\nO numero convertido para hexadecimal fica assim: {}{}{}'.format('\033[32m',hex(n), '\033[m'))