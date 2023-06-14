"""
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
"""
# Contador
print('{:=^52}'.format(''))
n = int(input("Informe um numero para receber o seu fatorial: "))
contador = n
r = 1
print("\nCalculando fatorial de {}! = ".format(n), end="")
while contador > 0:
    print("{} ".format(contador), end="")
    print("x " if contador > 1 else "=", end="")
    r *= contador
    contador -= 1
# Utilizando f ele transforma a chaves em uma f-string que vai analisar expressão e 
# substituirá certos valors, como aqui adicionando uma virgula , que é o caso.
print(f' {r:,}', end='')
print('\n{:=^52}\n'.format(''))


"""
n = int(input('\nDigite um numero para receber o seu fatorial: '))
c = n
r = 1
print('Calculando {}! = '.format(n),end='')
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
    r *=c
    c -= 1
print('{}'.format(r))
"""
