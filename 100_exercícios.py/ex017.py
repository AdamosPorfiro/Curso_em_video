'''
===== Exercicio 17 =====

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
calcule e mostre o comprimento da hipotenusa.

Analise criticamente: Para calcularmos o comprimento de uma hipotenusa é necessario saber os valores dos catetos adjacente e oposto, tendo 
essas informação elevamos os catetos ao quadrado c1² + c2² fazendo o caulculo fica Ex.: c1 = 3²= 3*3 = 9 e c2 = 4² = 4*4=16, logo, 9 + 16 = 25
pegamos o resultado final e fazemos a sua raiz quadrada: Extraimos a raiz quadrada de 25 = 5.83, etão teremos o valor da hipotenusa = 5

temos: comprimento da hipotenusa é de 5cm o teorema de pitagoras diz que: A soma dos quadrados dos catetos de um triangulo retangulo é igual o quadrado
de sua hipotenusa, logo temos: 5²=5*5=25, podemos fazer 25-quadrado de dos catetos = 25-16 = c1 = 9 o que sobra é de fato c2 = 16.

Metodo 5 Q's

1 - Quais são os dados de entrada?
-> input cateto_oposto;
-> input cateto_adjacente;

2 - O que devo fazer com esses dados?
-> Deve somar os catetos ao quadrado para encontrar o comprimento da hipotenusa.

3 - Quais são as restrições do programa?
-> Calculos de numero elevado a sua potência;
-> Raiz quadrada;
-> Soma

4 - Qual é o resultado esperado?
-> Exibir o comprimento da hipotenusa.

5 - Quais são os passos necessarios para alcançar o resultado?
#1 input cateto_oposto;
#2 input cateto_adjacente;
#3 calculo = cateto_oposto * cateto_oposto + cateto_adjacente * cateto_adjacente ** = resultado
#4 print resultado


'''
print('\n' + '=' * 8, 'Calculadora hipotenusa', '=' * 8)
from math import sqrt
c1 = int(input('Digite o cateto oposto\nCateto oposto: '))
c2 = int(input('\nDigite o cateto adjacente\nCateto adjacente: '))
resultado = (c1 * c1) + (c2 * c2)
print('\nCateto oposto é: {}\nCateto adjacente é: {}\nComprimento da hipotenusa é: {:.2f}'.format(c1, c2, sqrt(resultado)),'\n' + '=' * 40)