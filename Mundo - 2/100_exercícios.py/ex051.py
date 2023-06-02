'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos  dessa progressão.

Analise:

O que é o primeiro termo e a razão de uma PA?
R: PA significa progressão aritmética ela é uma sequêcia de elementos que é definida com base no seu primeiro termo e
a sua razão. O primeiro termo é definido como o primeiro elemento de um PA e a razão é a diferente entre os termos
subsequentes.

Por exemplo, temos a formula: x = a + r = x
x = É o resultado da progressão da nossa PA;
a = É o valor inicial definido pelo usuario;
r = É a razão que tambem é definida pelo usuario;

x = 2 + 3 = 5, logo x = 5
teremos o valor inicial de 2 e uma progressão de elementos somando 3 a cada progressão, gerando uma sequência de 
elementos com uma diferença de 3.
Resumindo a a sequência vai pulando de 3 em 3 elementos

Utilizando o termo = 2 e a razão = 3, temos uma sequencia:
2,5,8,11,14,17,20,23,26,29,22,25,28,31,34,37,40,43,46,49...

Quais são os dados de entrada?
input termo
input razão

O que devo fazer com esses dados?
Lê-los e exibir na tela os 10 primeiros termos dessa progressão aritmética

Quais são as restrições desse problema?
Exibir os 10 primeiros termos

Qual é o resultado esperado?
Exibir para o usuario a sequencia dos 10 primeiros termos com base nos dados informados

Quais são os passos para se alcançar o resultado?
input termo
input razão
for contador (10)
    for me dizer a PA (termo,0,razão)
'''
print('{:=^67}''\n{:^22}Progressão aritmética\n''{:=^67}'.format('','',''))
t = int(input('Informe o termo: '))
r = int(input('Informe a razão: '))
d = t + (10-1) * r
for c in range(t, d + r, r):
    print(c,' →', end= ' ')
print('TERMINOU')
print('{:=^67}'.format(''))