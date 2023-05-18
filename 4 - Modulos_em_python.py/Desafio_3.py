'''
===== Desafio 3 =====

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, 
cosseno e tangente desse ângulo.

Analise criticamente: Para calcular o o seno, cosseno e tangente usamos as formulas:

Seno = cateto_oposto / hipotenusa;
Cosseno = cateto_adjacente / hipotenusa; 
Tangente = cateto_oposto / cateto adjacente;

Primeiro precisamos encontrar o valor da hiptenusa através do calculo dos catetos elevado ao quadrado. Vamos ver no exemplo a seguir:
Cateto oposto: 3 cm logo, 3² = 3 * 3 = 9 cm;
cateto adjacente 4 cm logo, 4² = 4 * 4 = 16 cm;
9 + 16 = 25 
hipotenusa = raiz quadrada de 25 = 5, Então temos: 
Cateto oposto = 3cm; 
Adjacente = 4cm; 
Hipotenusa = 5cm;
Para provar que a hipotenusa esta correta o valor da hipotenusa ao quadrado corresponde aos catetos, fazemos a conta inversa sendo: 
5² = 5 * 5 = 25 - (3 * 3) = 16
5² = 5 * 5 - 25 - (4 * 4) = 9 
logo temos, 9 corresponde ao valor do cateto oposto ao quadrado e 16 que corresponde ao valor do cateto adjacente ao quadrado;

Agora podemos calcular seno, cosseno e tangente com as formulas acima:

seno = 3 / 5 = 0.6;
cosseno = 4 / 5 = 0.8;
tangente = 3 / 4 = 0.75;

'''
print('Calculadora de seno, cosseno e tangente')
from math import sin, cos, tan, radians
ang = float(input('\nDigite o angulo\nAngulo: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('\nO Seno é: {:.2f}\nO Cosseno é: {:.2f}\nA Tangente é: {:.2f}'.format(seno,coss,tang),'\n' + '=' * 40)