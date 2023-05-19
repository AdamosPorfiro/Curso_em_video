'''
Condições simples e composta

São expressões que avaliam se uma determinada condição é falsa ou verdadeira.
Ela controla um fluxo de execução do programa através de estrutura de controle
if/else/loops

No caso usaremos if / else = Se for, execute, senão, execute esse.

Estrutura condicional if/else

Ex: Se carro.esquerda()
        bloco_v_
    senão
        bloco_f_
===========================

    if carro.esquerdo():
        bloco True
    else:
        bloco False


'''
'''
#Exemplo de fluxo de execução:

tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print('O seu Carro é novo') # Fluxo 1 - Se a condição for verdadeira ele vai executar esse comando e o print fim, senão;
else:
    print('O seu Carro é velho') # Fluxo 2 - Senão, se a condição acima for falsa ele vai executar esse comando e o print final;
print('--FIM--') # O print final sempre é implementado no final do código independente do fluxo tomado;

#Pratica - 1
n=str(input('Digite o seu Nome: '))
if n == 'Adamos':
    print('\nQue nome lindo você tem!')
else:
    print('\nO Seu nome é tão normal!')
print('Bom dia, {}!!!'.format(n))
'''
#Pratica - 2
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('\nA sua média foi {:.1f}'.format(media))
if media >= 6.0:
   print('Sua média foi boa! PARABÉNS')
else:
   print('Sua média foi ruim! ESTUDE MAIS!')
#Forma simplificada
#print('Parabéns'if media>=6 else 'Estude mais')