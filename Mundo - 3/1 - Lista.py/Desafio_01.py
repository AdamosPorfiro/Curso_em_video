'''
Faça um programa que leia 5 valores númericos e guarde em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

Lembrando que caso algum numero seja repetido ele vai mostrar a posição de ambos os valores. 
'''
# Digita os valores e armazena na lista de números;
l_n = []
for r in range(5):
    n = int(input('Informe um numero: '))
    l_n.append(n)

# Criamos variaveis
maior = p_ma = p_me = 0 # Maior = maior numero | p_ma = posição maior núm | p_me = posição do menor núm
menor = l_n[0] # Menor é iniciada como o 1º número armazenado na lista de números;
i_ma = [] # Lista vazia que vai armazenar o indice do maior número;
i_me = [] # Lista vazia que vai armazenar o indice do menor número;
for i,num in enumerate(l_n): # Vamos acessar cada número e seus respectivos indices
    if num > maior: # Se o numero da lista de numeros foi maior que o valor iniciado na variavel maior ele faz;
        maior = num # Se true então maior passa a ser o num
        i_ma = [i] 
    elif num == maior: # Se o proximo numero for igual o valor armazenado em maior, ele executa
        i_ma.append(i) # E armazena esse valor na variavel corretamente
    if num < menor: # A mesma coisa acontece para a variavel menor
        menor = num
        i_me = [i]
    elif num == menor:
        i_me.append(i)
print(f'''Você digitou os números: {l_n}\nO maior número digitado foi {maior} e sua posição é {i_ma}
O menor número digitado foi {menor} e sua posição é {i_me}''')
    #print(f'Indice {i}\números da lista {ma}')

