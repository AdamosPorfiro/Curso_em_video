'''
Crie um programa que leia varios números inteiros pelo teclado. 
O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada.
No final mostre quantos numeros foram digitados e qual foi a soma entre eles.
(Desconsiderando o flag)
'''
print("-="*20)
print("{:>25}".format(" Desafio 64 "))
print("-="*20)
flag = 0
qtd_numeros = 0
somatorio = 0
while flag != 999:
    n = int(input("Informe um número [999 - sair]: "))
    if n == 999:
        flag = 999
    else:
        qtd_numeros += 1
        somatorio += n
print(f"Você digitou {qtd_numeros} números\nA soma de todos dos número digitados é {somatorio}")
print("-="*20)