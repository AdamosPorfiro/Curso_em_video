'''
Refaça o desafio 035 dos triangulos acrescentando o recurso de mostrar que tipo
de triangulo será formado:

- Equilátero: Todas os lados iguais;
- Isosceles: Dois lados iguais;
- Escaleno: Todos os lados diferentes;

Enunciado do ex035: 

Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem
ou não formar um triângulo.

Ex.:

R1 - -------- 
R2 - -------------
R3 - -----------------

===============================================================================
Desigualdade triangular:

Diz que para formar um triangulo com três retas é necessario que duas retas, sejam maiores que a terceira, logo se
obtemos:

A|B|C então:
A + B > C = True;
A + C > B = True;
B + C > A = True;

1|2|3
1 + 2 >= 3 True;
1 + 3 >= 2 True;
2 + 3 >= 1 True;
CASO ESSAS REGRAS SEJAM ATENDIDAS, ENTÃO PODEMOS TER UM TRIANGULO COM TRÊS RETAS.

Equilátero:
1 - Todas as retas devem possuir o mesmo comprimento;
CASO ESSA REGRA SEJA ATENDIDA, ENTÃO PODEMOS TER UM ISOSCELE.

Isosceles:
1 - Pelo menos duas retas devem ter o mesmo comprimento;
2 - A soma de duas retas resulta em um numero maior que a medida da terceira;
CASO ESSAS REGRAS SEJAM ATENDIDAS, ENTÃO PODEMOS TER UM ISOSCELES.

Escaleno: 
1 - Todas as retas devem ter comprimentos diferentes; 
2 - A soma de duas retas devem ser maior que a terceira;
CASO ESSAS REGRAS SEJAM ATENDIDAS, ENTÃO PODEMOS TER UM ESCALENO.
=================================================================================

1 - Quais são os dados de entrada?
input reta1
input reta2
input reta3

2 - O que devo fazer com esses dados?
Comparar e calcular os comprimentos e exibir se é possivel formar um triangulo com as três retas
e em seguida exibir qual tipo de triangulo é possivel formar com esses valores, sendo eles:
Equilátero, Isosceles, Escaleno;

3 - Quais são as restrições desse problema?
São três retas de valores reais;
Validar se é possivel formar um triangulo;
Equilatero, isoceles, escaleno;

4 - Qual é o resultado esperado?
Exibir na tela se é possivel forma um triangulo com os dados informados e qual triangulo é possivel formar;

5 - Quais são os passos para se alcançar o resultado esperado?
input reta1;
input reta2;
input reta3;
if reta1 + reta2 >= reta3 and reta1 + reta3 >= reta2

'''

