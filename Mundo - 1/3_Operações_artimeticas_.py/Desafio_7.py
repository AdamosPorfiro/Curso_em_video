"""
Desafio 7 

Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

A media é calculada da seguinte forma:

Soma dos numeros divido ela quantidade de numero Ex: 1 2 3 4;
1+2+3+4 = 10
10/4 = 2.5
Media = 2.5

5 Q's

1 - Quais os dados de entrada?
  - Dois numero

2 - O que devo fazer com esses dados?
  - Calcular a media de um aluno

3 - Quais são as restrições do programa?
  - Apenas para calcular a media

4 - Qual o resultado esperado?
  - A media final do aluno

5 - Quais os passos necessarios para alcançar o resultado esperado?

  - nota_1 e nota_2
  - media = (nota_1+nota_2)/2
  - print A media do aluno é media
"""

print("{:=^28}".format(" Desafio 7 "))
n_1 = float(input("Digite a primeira nota: "))
n_2 = float(input("Digite a segunda nota: "))
media = (n_1+n_2)/2
print("A média é {:.2f}".format(media))
print("{:=^28}".format(""))
