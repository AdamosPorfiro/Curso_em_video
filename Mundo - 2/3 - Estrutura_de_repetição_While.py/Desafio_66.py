'''
Crie um programa que leia varios numeros inteiros pelo teclado.
O programa só vai parar quando o usuario digitar 999, que é a condição de parada.
No final mostre quantos numeros foram digitados e a soma entre eles.

(Desconsiderando o FLAG)

'''
print("{:>14}".format("Desafio 66"))
qtd_numeros = soma = flag = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    soma += n
    qtd_numeros +=1
print(f"Você digitou {qtd_numeros} números\nA soma entre os número é {soma}")