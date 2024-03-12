'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero
até vinte. Seu programa deverá ler um numero pelo teclado(entre 0 e 20) e mostra-lo por extenso.
'''

contagem_por_extenso_0_a_20 = (
    'zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
    'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'
                              )
while True:
    numero = int(input("Digite um número: "))
    for pos,num in enumerate(contagem_por_extenso_0_a_20):
        if numero == pos:
            print(f"{num}")
    continuar = str(input("Deseja continuar [S | N]: ")).strip().upper()
    if continuar == 'N':
        break
