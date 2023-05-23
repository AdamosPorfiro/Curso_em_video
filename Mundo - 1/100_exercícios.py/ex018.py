'''
===== Exercício 18 =====

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
print('\nCalculadora de seno, cosseno e tangente')
from math import sin, cos, tan, radians
angulo = float(input('\nDigite o ângulo\nÂngulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('\nO seno é: {:.2f}.\nO cosseno é: {:.2f}.\nO tangente é: {:.2f}.'.format(seno,cosseno,tangente),'\n' + '=' * 40)
