'''
Faça um programa que leia 5 valores númericos e guarde em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

Lembrando que caso algum numero seja repetido ele vai mostrar a posição de ambos os valores. 
'''
l_n = []
for cont in range(5):
    n = int(input('Digite um número: '))
    l_n.append(n)
n_maior = 0
n_menor = l_n[0]
p_maior = []
p_menor = []
for pos,num in enumerate(l_n):
    if num > n_maior:
        n_maior = num
        p_maior = [pos]
    elif num == n_maior:
        p_maior.append(pos)
    if num < n_menor:
        n_menor = num
        p_menor = [pos]
    elif num == n_menor:
        p_menor.append(pos)
print(f'Você digitou os número {l_n}\nO maior número é {n_maior} nas posições {p_maior}\nO menor número é {n_menor} nas posições {p_menor} ')