'''
Crie um programa que simule o funcionamento de um caixa eletronico.
No inicio, pergunte ao usuario qual será o valor a ser sacado (numero inteiro)
e o programa vai dizer quantas cedulas de cada valor serão entregues.

OBS: Considere que  o caixa possui cedulas de:
R$50 R$20 R$10 e R$1

Vamos desenvolver um loop infinito que irá repetir todo o bloco;
'''
print('\n{:=^30}\n{:>7}BANCO DO ADAMOS\n{:=^30}'.format('','',''))
saque = int(input('Qual o valor a ser sacado R$ '))
total_ced = 0
ced = 50
while True:
    if saque >= 50:
        saque -= ced
        total_ced+=1 
        print(f'Cedulas R$ 50: {total_ced}')
        if total_ced < 50:
            ced = 20
            total_ced+=1
             
    if saque < 50:
        break
print(f'Quantidade de cédulas de R$ 50: {total_ced} cédulas') 





