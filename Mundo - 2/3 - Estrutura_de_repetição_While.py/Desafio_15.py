'''
Crie um programa que simule o funcionamento de um caixa eletronico.
No inicio, pergunte ao usuario qual será o valor a ser sacado (numero inteiro)
e o programa vai dizer quantas cedulas de cada valor serão entregues.

OBS: Considere que  o caixa possui cedulas de:
R$50 R$20 R$10 e R$1
'''
print('\n{:=^30}\n{:>7}BANCO DO ADAMOS\n{:=^30}'.format('','',''))
saque = int(input('Qual o valor a ser sacado R$ '))
total = saque
total_ced = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        total_ced+=1 
    else:
        if total_ced > 0:
            print(f'Total {total_ced} cédulas de R$ {ced}') 
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break






