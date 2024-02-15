"""
Desafio 8

Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

5 Q's

1 - Quais os dados de entrada?
- Numero decimal

2 - O que devo fazer com esses dados?
- Converte-lo em centimetros e em milimetros

3 - Quais as restrições do programa?
- Nenhum

4 - Qual o resultado esperado?
- Exibir na tela o valor informado em metros convertido em centimetros e milimetros

5 - Quais são os passos para se alcançar o resultado esperado?
- Valor_metros
- cent = valor_metros*100
- mil = valor_metros*1000
- print = Metro informado é valor_metros convertido para centimetros é cent e para milimetros é mil
"""
from time import sleep
print("{:=^42}".format(" Desafio 8 "))
v_metros = float(input("Informe quantos metros quer converter: "))
centimetros = v_metros*100
milimetros = v_metros*1000
print("Convertendo para centimentros e milimetros...")
sleep(2)
print("\n\nCentimentros: {}\nMilimetros: {}".format(centimetros, milimetros))
print("{:=^42}".format(""))