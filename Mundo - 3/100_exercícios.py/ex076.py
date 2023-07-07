'''
Crie um programa que tenha várias palavras(Não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

Palavras = ('Cantar', 'Sabonete', 'Montanha', 'Arvores')
for p in Palavras:
    vogais = ''
    for v in p:
        if v.lower() in 'aeiou':
            vogais+=v
    print(f'A palavra {p} tem as vogais \033[41m{vogais}\033[m')
    '''
Palavras = ('Cantar', 'Sabonete', 'Montanha', 'Arvores')
for p in Palavras:
    print(f'\nNa palavra {p.upper()} temos: ',end='')
    for l in p:
        if l.lower() in 'aeio':
            print(f'{l}',end='')