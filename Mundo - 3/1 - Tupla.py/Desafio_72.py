'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero
até vinte. Seu programa deverá ler um numero pelo teclado(entre 0 e 20) e mostra-lo por extenso.
'''
from time import sleep
contagem_por_extenso_0_a_20 = (
    'zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
    'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'
                              )
print("-="*15)
print("{:>20}".format(" Desafio 72 "))

while True:
    print("-="*15)
    while True:
        numero = int(input("Digite um número [0 á 20]: "))
        if numero < 0 or numero > 20:
            continue #Continua executando o while
        else:
            break
    for pos,num in enumerate(contagem_por_extenso_0_a_20):
        if numero == pos:
            print(f"Você digitou o número {num}")
            print("-="*15)
    continuar = str(input("Deseja continuar [S | N]: ")).strip().upper()
    if continuar == 'N':
        break
print("Saindo...")
sleep(1)
print("Obrigado por usar nosso programa, volte sempre!")
