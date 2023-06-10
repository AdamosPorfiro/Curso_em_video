'''
Faça um programa que leia um numero qualquer e mostre o seu fatorial.

Ex: 5! = 5x4x3x2x1= 120

Quais são so dados de entrada?
input numero

O que devo fazer com esses dados?
Exibir na tela o fatorial de input numero

Quais são as restrições desse problema?
Fatorial de um numero

Qual o resultado esperado?
Exibir na tela o fatorial do numero digitado

Quais são os passos para se alcançar o resultado?
input numero
sair = 2
fatorial = 0
while sair == 2
    input numero
    for c in range(0,numero)
        fatorial *= c
    print Fatorial do numer {numero} = {}
    sair = input 1 - sair do programa  2 - continuar

acumulador = 1
n = int(input('\nInforme um numero para receber o seu fatorial:  '))
for item in range(n,0,-1):
    acumulador *= item
print('\nO fatorial do número {} é {}'.format(n ,acumulador))
'''
acumulador = 1 
contador = 0
n = int(input('\nInforme um numero para receber o seu fatorial:  '))
while contador < n:
    contador += 1
    acumulador *= contador
print('O fatorial do numero {} é {}'.format(n,acumulador))

        
      