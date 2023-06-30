'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero
até vinte. Seu programa deverá ler um numero pelo teclado(entre 0 e 20) e mostra-lo por extenso.

Dados de entrada?
1 tupla totalmente preenchida com um contagem escrita por extenso, do numero zero ao vinte!


'''
n_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 
             'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 
             'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
             'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
             'Dezenove', 'Vinte')
n = int(input('Digite um número entre 0 e 20: '))
for cont in n_extenso:
    