"""
Crie um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50.

Como é calculado matematicamente os numeros pares?
R:  Um numero é par quando ele é divisivel por 2 e o resto da sua divisão é 0 Ex: 2784% 2 = 0 Portanto 2784 é par.

"""
print('Numeros pares')
for con in range(2, 51, 2):
    print(con, end=' ')