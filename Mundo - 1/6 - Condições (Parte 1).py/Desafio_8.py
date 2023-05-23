'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem
ou não formar um triângulo.

Ex.:

R1 - -------- 
R2 - -------------
R3 - -----------------

Analise: Para formar um triangulo é necessario três retas, vamos levar em consideração um regra importante para isso: 
A desigualdade triangular que diz que: Para que tês retas formem um triangulo, é necessario que duas dessas retas sejam
maiores que a terceira, esse é o principio da DESIGUALDADE TRIÂNGULAR.

Ex: Se obtemos as retas A|B|C então:
A + B > C ;     
A + C > B;
C + B > a;

Se todas as condições, forem verdadeiras, então podemos formar um triangulo:

Ex: Se obtemos as seguintes retas: A = 5 | B = 10 | C = 7 então:
5 + 10 > 7 = VERDADEIRO;
5 + 7 > 10 = VERDADEIRO;
10 + 5 > = 7 VERDADEIRO;

R.: É possivel formar um triângulo utilizando essas medidas;

1 - Quais são os dados de entrada?
- input m1, m2, m3;

2 - O que devo fazer com esses dados?
- Deve ler e exibir se é possivel formar um triângulo ou não;

3 - Quais são as retrições do problema?
- Nenhuma;

4 - Qual o resultado esperado?
- Exibir se é possivel formar um triângulo ou não;

5 - Quais são os passos necessarios para se alcançar o resultado esperado?
1 - input m1, m2, m3;
2 - if m1 + m2 > m3 e m1 + m3 > m2 e m2 + m3 > m1 
        print Sim, é possivel formar um triangulo com essas medidas!
    else:
        print Não é possivel formar um triangulo com essas medidas!

'''
print('\n' + '-=-' * 18)
print(' ' * 5, 'Analisando os segmentos de um triângulo')
print('' + '-=-' * 18)
m1 = float(input('Informe o primeiro segmento\n segmento 1: '))
m2 = float(input('Informe o segundo segmento\n segmento 2: '))
m3 = float(input('Informe o terceiro segmento\n segmento 3: '))

if m1 + m2 > m3 and m1 + m3 > m2 and m3 + m2 > m1:
    print ('\nSim, é possivel formar um triangulo com essas medidas')
else:
    print('\nNão é possivel formar um triangulo com essas medidas')
print('\n' + '-=-' * 18)