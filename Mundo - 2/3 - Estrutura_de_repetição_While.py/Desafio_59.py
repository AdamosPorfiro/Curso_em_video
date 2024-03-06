'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
 Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
n1 = int(input("Informe o 1° número: "))
n2 = int(input("Informe o 2° número: "))
opções = 0
while opções != 5:
    print("""
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair""")
    opções = int(input("Escolha opção: "))
    if opções == 1:
        somar = n1 + n2
        print(f"A soma entre o valor {n1} + {n2} é {somar}")
    elif opções == 2:
        produto = n1 * n2
        print(f"O produto entre o valor {n1} x {n2} é {produto}")
    elif opções == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"O maior número entre {n1} e {n2} é {maior}")
    elif opções == 4:
        print("=-"*10)
        n1 = int(input("Informe o 1° número: "))
        n2 = int(input("Informe o 2° número: "))
    elif opções == 5:
        print("Fechando...")
        sleep(1.5)
    else:
        print("Opção invalida, digite novamente!")
    print("-="*10)
print("Programa fechado, Volte sempre!")

'''
from time import sleep
print("-="*20)
print("{:>25}".format(" Desafio 60 "))
print("-="*20)
opções = 0
n1 = n2 = 0
print("="*40)
while opções != 5: 
    if opções == 4:
        while opções == 4:
            n1 = int(input("Digite o 1° valor: "))
            n2 = int(input("Digite o 2° valor: "))
            opções = 0
            break
    else:
        n1 = int(input("Digite o 1° valor: "))
        n2 = int(input("Digite o 2° valor: "))
    while opções == 0 or opções == 1 or opções == 2 or opções == 3:  
        print("""
            [1] Somar
            [2] Multiplicar
            [3] Maior
            [4] Novos números
            [5] Sair do programa
                """)
        opções = int(input("Escolha: "))
        #Somar
        if opções == 1:
            soma = n1 + n2
            print(f"A soma dos valores {n1} + {n2} = {soma}")
            #print(f"A soma dos valores {n1} + {n2} = {n1+n2}")
        #Multiplicação
        elif opções == 2:
            multiplicação = n1 * n2
            print(f"A multiplicação dos valores {n1} x {n2} = {multiplicação}")
            #print(f"A multiplicação dos valores {n1} x {n2} = {n1*n2}")
        #Maior
        elif opções == 3:
            if n1 > n2:
                print(f"O maior número é o 1° valor = {n1}")
            else:
                print(f"O maior número é o 2° valor = {n2}")
        #Novos números
        elif opções == 4:
            print("Informe novos valores!")
        #Sair do programa
        elif opções == 5:
            opções = True
            print("Saindo do programa...")
            sleep(1)
            print("Obrigado, Volte sempre!")
        else:
            print("Opção invalida!!! Digite novamente.")
        print("="*40)
'''