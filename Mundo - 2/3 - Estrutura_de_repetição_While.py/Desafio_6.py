"""
Melhore o DESAFIO 51, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""
'''
print("{:=^60}\n{:^18}PROGRESSÂO ARITMÉTICA\n{:=^60}".format("", "", ""))
n1 = int(input("{:^20}Informe o termo: ".format("")))
n2 = int(input("{:^20}Informe o razão: ".format("")))
contador = 0
termo = n1
print("\n{:^10}Os 10 primeiros termos dessa progressão é:\n".format(""))
while contador < 10:
    print("{:^4}➝ ".format(termo), end="")
    contador += 1
    termo += n2
print("FIM")
reiniciar = 1
while reiniciar == 1:
    reiniciar = int(input("""
                \nDeseja ver mais termos? 
                        [0] - não  
                        [1] - sim
                        Escolha: """))
    if reiniciar == 0:
        reiniciar= 0
        print("{:^24}Obrigado!".format(""))
    else:
        n3 = int(input('Quantos termos mais quer ver? '))
        contador_1 = 0
        termo_1 = termo-2
        print('\nOs',f'{n3}','termos dessa progressão é:')
        while contador_1 < n3:
            termo_1+=n2
            contador_1+=1
            print('{:^4}➝ '.format(termo_1),'FIM' if contador_1 == n3  else '',end='')
print("{:=^60}".format(""))
'''
print('Gerador de PA\n{:=^20}'.format(''))
n1 = int(input('Informe o termo: '))
n2 = int(input('Informe o razão: '))
termo = n1
for c in range(1,11):
    termo += n2
    print(f'{termo}➝ ', end='')
print('PAUSA')
n3 = 1
while n3 != 0:
    n3 = int(input('Quantos termos mais deseja mostrar? [0 - sair] '))
    c = 0
    while c  < n3:
        termo+=n2
        print(f'{termo}➝ ', end='')
        c+=1
        if c==n3:
            print('PAUSA')
    if n3 == 0:
        print('Obrigado!')
    

    
