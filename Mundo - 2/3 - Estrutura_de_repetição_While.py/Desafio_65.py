'''
Crie um programa que leia vários números inteiros pelo teclado.
 No final da execução:
 - mostre a média entre todos os valores 
 - qual foi o maior e o menor valor lidos.
O programa deve perguntar ao usúario se ele quer ou não continuar a digitar valores.
'''
print("-="*20)
print("{:>25}".format(" Desafio 65 "))
print("-="*20)
continuar = True
Divisor_media = 0
Soma_valores = 0
maior = 0
menor = 0
while continuar != False:
    print("-="*10)
    n = int(input("Informe um número: "))

    #Maior e menor
    if n > maior:
        maior = n
    if menor == 0:
        menor = n
    if  n < menor:
        menor = n

    #Média
    Divisor_media += 1
    Soma_valores += n

    #Continuar ou não
    continuar = str(input("Deseja sair [S/N] ")).upper()
    print("-="*10)
    if continuar in "S":
        continuar = False

print(f"Você digitou {Divisor_media} e a média é de {Soma_valores/Divisor_media:.2f}")
print(f"O maior número é {maior} e o menor é {menor}")
print("-="*20)