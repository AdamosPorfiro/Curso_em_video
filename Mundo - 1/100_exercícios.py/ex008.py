'''
===== Exercicio 8 =====

Escreva um programa que leia o valor em metros e o exiba convertido em centimetros e milimetros.

Analise criticamente:
-> 1 m² = À uma area de 1x1 ou seja, 2 metros total;
-> 1 m = 100 cm, logo 1m² equivale a 200cm, lembrando que a area é de 1x1
-> 1 m = 100 cm, 1 cm possui 10 mm logo temos 1000 mm para 100 cm formula: mm = 100 * 10 = 1000 mm em uma area de 1m² = 2000 mm

Metodo 5 Q's

1 - Quais são os dados de entrada?
-> input n1_metro

2 - O que deve ser feito com esses dados?
-> Devem exibir os dados digitado, convertidos em centímetros e milímetros.


3 - Existe alguma restrição nesse problema?
-> Numeros reais ;
-> Serão Convertidos para centimentros e milimetros.

4 - Qual o resultado esperado?
-> Os dados devem ser exibidos e convertidos em centimetros e milimetros.

5 - Qual é a sequência de passos a ser feito para se alcançar o resultado esperado?
1 - input n1_m²
2 - print n1_m² * 10.000 e n1_m² * 10.000 * 100

'''
print('\n'+'=' * 22, 'Desafio 4', '=' * 22,'\n', ' ' * 2, 'Conversor de m² para centimetro e milimetro',' ' * 3)
m1 = float(input('\nQuantos m² quer que sejam convertidos?\nM²: '))
print('\n{:.2f} m² é equivalente a uma area de {:.2f}x{:.2f} metros que possuem um total de {:.1f} em cm e {:.1f} em mm'.format(m1, m1, m1, m1 * 2 * 100, m1 * 2 * 100 * 10),'\n'+'=' * 54)