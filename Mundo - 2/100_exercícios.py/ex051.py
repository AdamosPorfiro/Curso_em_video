'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos  dessa progressão.
'''
print('\nProgressão aritmética\n')
t = int(input('Informe o termo: '))
r = int(input('Informe a razão: '))
print(t)
for c in range(10):
    t = t + r
    print(t)
print('{:=^22}'.format(''))