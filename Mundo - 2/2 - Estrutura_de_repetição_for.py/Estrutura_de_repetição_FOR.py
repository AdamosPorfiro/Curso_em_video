'''
Estrutura de repetição FOR

FOR = Permite executar uma bloco de códigos repetidamente para uma sequência de elementos ou uma coleção de elementos, chamamos em
de variavel de laço de variavel de controla, laço de repetição ou laço.

Ex.: 

Ele vai executar 10 passos de 1 a 10, quando chegar no passo 10 ele vai sair do laço e executar pega:

laço c no intervalo(1,10)
    passo
pega

Representação no py:

for c in range(1,10):
    passo
pega

Tambem podemos usar estruturas de condição dentro de estruturar de reopetição:

laço c no intervalo de (0, 3)                       laço c in intevalo (0 , 3)
    se objeto                                                   if objeto
        pega                                                        pega
    passo                                                        passo
    pula                                                           pula
passo                                                         passo
pega                                                           pega

'''

for c in range(0,6):
    print('oi')
print('fim')


for c in range(6, 0, -1):
    print(c)
print('fim')
'''
for c in range(0, 10, 2): # Vai contar de 0 a 10 pulando de 2 em 2
    print(c)
print('fim')


n = int(input('Digite um numero: '))
for c in range(0, n+ 1):
    print(c)
print('FIM')


s = 0
for c in range(0,3):
    n = int(input('Informe numero: '))
    s += n
print('O somatório de todos os numero resulta em {}'.format(s))

'''