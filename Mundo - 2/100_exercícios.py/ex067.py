'''
Faça um programa que faça a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
O programa será interronpido quando o valor digitado for negativo.

Dados de entrada: input numero

O que fazer com os dados: Exibir a tabuada do input numero

Restrições: O programa só será interronpido quando o valor digitado for negativo

Resultado: Exibir a tabuada de cada valor digitado pelo usuario

Passo a passo:
print TABUADA
while true
    input usuario
    for c in range(1,11)
        print input x c = input*c  
    if input < 0
        break
print Obrigado, volte sempre!
'''
print('\n{:~^20}\n{:>6}TABUADA\n{:~^20}'.format('','',''))
while True:
    print('\n{:>3}Para sair [-1]'.format(''))
    n = int(input('Informe um número: '))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n:>5} x {c:2} = {n*c:3}')
print('Obrigado, volte sempre!')
