'''
Crie um programa que leia varios números inteiros pelo teclado. 
O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada.
No final mostre quantos numeros foram digitados e qual foi a soma entre eles.
(Desconsiderando o flag)

1 Quais são os dados de entrada?
input numero

2 O que devo fazer com esses dados?
Exibir quantos numeros foram digitados;
Exibir soma entre esses numero;
Deve desconsiderar o numero o flag dessa analise (Condição de parada).

3 Quais são as restrições desse problema?
Deve desconsiderar o numero flag da analise;
Numero devem ser inteiros;

4 Qual o resultado esperado?
Ler os numeros digitados;
Exibir quantidade de numeros que foram digitados;
Exibir a soma desses numeros;
Desconsiderar o numero 999 sendo que ele é o flag;

5 Quais são os passos necessarios para se alcançar o resultado esperado?

saida = 999
contador_n = 0
soma = 0
while saida != 999
    n1 = input numero
    if n1 == 999:
        print Analise final...
        saida = 999
    else:
        contador += 1
        soma += n1
print Quantidade de numero digitados: {contador}
print Soma dos numeros digitado: {soma}
'''
from time import sleep
sair = 0
contador_n = 0
soma = 0
while sair != 999:
    n1 = int(input('Digite um numero ou para sair digite (999):  '))
    if n1 == 999:
        print('Analise final...')
        sleep(1)
        sair = 999
    else: 
        contador_n += 1
        soma += n1
print('Quantidade de números digitados foi de {} números\nA soma de todos os números digitados é {}\nObrigado!'.format(contador_n,soma))


