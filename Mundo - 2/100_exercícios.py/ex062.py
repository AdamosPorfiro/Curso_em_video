'''
Melhore o DESAFIO 51, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''
print('{:=^60}\n{:^18}PROGRESSÂO ARITMÉTICA\n{:=^60}'.format('','',''))
reiniciar = 1
while reiniciar == 1:
    n1 = int(input('{:^20}Informe o termo: '.format('')))
    n2 = int(input('{:^20}Informe o razão: '.format(''))) 
    contador = 0
    print('\n{:^10}Os 10 primeiros termos dessa progressão é:\n'.format(''))
    while contador < 10:
        termo = n1 + contador*n2
        print('➝ {:^4}'.format(termo),end='')
        contador += 1
    reiniciar = int(input('''
                \nDeseja ver mais termos? 
                        [0] - não  
                        [1] - sim
                        Escolha: '''))
    if reiniciar == 0:
        print('{:^24}Obrigado!'.format(''))
    print('{:=^60}'.format(''))