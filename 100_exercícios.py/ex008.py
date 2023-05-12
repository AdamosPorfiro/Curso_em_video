'''
===== Exercício 8 =====

Escreva um programa que leia o valor em metros e o exiba convertido em centimetros e milimetros.

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
print('=' * 20, 'Exercício 8', '=' * 20)
print (' ' * 4, 'Conversor de m² para centimetro e milimetro',' ' * 4)
m1 = float(input('\nQuantos m² quer que sejam convertidos?\nM²: '))
print('\n{} m² é equivalente a {} cm que possui {} mm'.format(m1, m1 * 10000, m1 * 10000 * 10))