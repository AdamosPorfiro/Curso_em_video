'''
===== Desafio 10 =====

Escreva um programa que converta graus celsius para fahrenheit 

Analise criticamente: 1 graus celsius equivale a 1.8 graus fahrenheit, a formula que usamos para fazer a conversão é:

f = (c * 9/5) + 32

f -> Fahrenheit
c -> Celsius
9/5 -> 1.8 o equivalente de 1 graus em fahrenheit
32 -> Compensar o deslocamento de 0 entre as duas escalas, 32 é o ponto de congelamento da água em fahrenheit e celsius e 0

Metodo dos 5 Q's

1 - Quais são os dados de entrada?
-> input g_c.

2 - O que deve ser feito com esses dados?
-> Deve ser convertidos para fahrenheit utilizando a formula: f=(c * 9/5)+32;
-> QUe a conversão seja exibida para o usuario na tela.

3 - Quais são as restrições desse problema?
-> Numeros reais, com decimais;
-> Conversão de temperatura utlizando formula especifica.

4 - Quais são os resultados esperados?
-> Que a conversão seja feita corretamente e exiba o resultado para o usuario.

5 - Quais são os passos necessarios para se alcançar o resultado?
-> input g_c
-> print (g_c * 9/5) + 32

'''
print('\n','=' * 1, 'Conversor de celsius para fahrenheit','=' * 1,'\n\n'+'Para separar os decimais use ponto Ex.: 31.5')
g_c = float(input('\nDigite quantos graus celsius quer converter\nC°: '))
print('\n{:.2f}c° graus celsius corresponde a {:.2f}f° fahrenheit'.format(g_c, ((g_c*9)/5)+32),'\n'+'=' * 51)