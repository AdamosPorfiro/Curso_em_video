'''
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando WHILE

Ex: T = 5 R = 2
PA = T+R
5 > 7 > 9 > 11 > 13 > 15 > 17 > 19 > 21 > 23
'''
print('{:=^60}\n{:^18}PROGRESSÂO ARITMÉTICA\n{:=^60}'.format('','','')) # TITULO;
n1 = int(input('{:^20}Informe o termo: '.format(''))) # INPUT;
n2 = int(input('{:^20}Informe o razão: '.format(''))) # INPUT;
t = n1
contador = 0 # CONTADOR DE 0 A 10;
print('\n{:^10}Os 10 primeiros termos dessa progressão é:\n'.format('')) # EXIBIR
while contador < 10: # EM QUANTO O CONTADOR FOR MENOR QUE 10 O BLOCO ABAIXO SERÁ EXECUTADO;
    print('➝ {:^4}'.format(t),end='') # EXIBI OS TERMOS
    contador += 1 # SOMA MAIS UM NO CONTADOR
    t += n2
print('FIM!')
print('\n{:=^60}'.format(''))
