'''
O que é uma estrutura de repetição WHILE?
R: È um estrutura de controle de fluxo que permite repetir
um bloco de códigos em quanto uma condição for verdadeira ou falsa;

Utilizamos while com frequencia quando não sabemos o limite de uma repetição
por exemplo, se é necessario 20 passos para alcançar um objeto, é mais
pratico usarmos a estrutura FOR, caso não soubessemos a quantidade de passos
então usariamos o WHILE.

Ex.: 
Em quanto maça == false
    passo
pega
=======================
While apple == false
    passo
Pega
'''
'''for c in range(1,3):
    print(c)
print('Fim')

c = 1 #Inicio variavel com 1
while c < 10: # Em quanto c for menor que 10 execute
    print(c) #Vamos exibir (c)
    c = c+1 # Em seguida ele vai somar +1 em c; 
print('Fim') # Exibi fim ao final da estrutura de repetição c;
#Toda vez que passar pela estrutura ele vai somar +1 a c até chegar em
1#10, Quando chegar em 10, ele sai da estrutura e exibi o fim.

for c in range(1,5):
    n = int(input('Digite um numero: '))
print('Fim')

n = 1
r = 'S'
while r == 'S':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''

n = 1
qtd_p = 0
qtd_i = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n!=0:
        if n%2 == 0:
            qtd_p += 1
        else:
            qtd_i += 1
print('Você digitou {} numeros pares e {} numeros impares'.format(qtd_p, qtd_i))