'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero
até vinte. Seu programa deverá ler um numero pelo teclado(entre 0 e 20) e mostra-lo por extenso.

Quais são os dados de entrada?
1 tupla totalmente preenchida com uma contagem escrita por extenso, do numero zero ao vinte!
1 input numero_usuario

O que fazer com esses dados de entrada?
Com base no input numero_usuario vamos acessar o elemento dentro da tupla que corresponde ao
numero que o usuario digitou.

Qual é a restrição desse probemas?
Os inputs do usuario e os elementos da tupla vão de 0 á 20

Qual é o resultado esperado?
É receber o input numero_usuario e escrever na tela por extenso esse numero

Quais são os passos para se alcançar o resultado esperado?
Numero_em_exentenso = ('zero' a 'vinte')
input Numero_do_usuario
for indice,num in enumerate(Numero_em_extenso)
    if n == indice:
        print num
'''
n_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 
             'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 
             'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
             'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
             'Dezenove', 'Vinte')
continuar = 'S'
while continuar == 'S':
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novemente! ', end='')
    print(f'Você digitou o numero \33[32m{n_extenso[n]}\33[m')
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]