'''
Crie um programa que leia varios numeros inteiros pelo teclado.
O programa só vai parar quando o usuario digitar 999, que é a condição de parada.
No final mostre quantos numeros foram digitados e a soma entre eles.

(Desconsiderando o FLAG)

Dados de entrada: Input teclado

O que fazer: O programa vai ler os numeros digitado até que o usuario pare o programa,
quando o programa for parado ele vai exibir a quantidade de numeros digitado e a soma entre eles.

Restrição: Condição de parada é 999 que deve ser desconsiderada da analise

Resultado: O programa vai ler os numeros digitado até que o usuario pare o programa,
quando o programa for parado ele vai exibir a quantidade de numeros digitado e a soma entre eles.

Passo a passo:
s = c = 0
while input != 999
    input usuario
    if input == 999
        break
    c += 1
    s += input
print Quantidade de números digitados: c
print Soma entre os números informados: s
'''

s = c = n = 0
while True:
    n = int(input('Digite um numero [999 pra parar]: '))
    if n == 999:
        break
    s += n
    c+=1
print(f'\nQuantidade de números digitados: {c}\nA soma entre os números digitados:{s}')