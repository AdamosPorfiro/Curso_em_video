'''
Crie um programa que tenha várias palavras(Não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

Palavras = ('Sabonete', 'Aroma', 'Chinelo', 'Porta retrato', 'Presente', 'Placa', 'Sacola')
for p in Palavras:
    vogais = ''
    for l in p:
        if l.lower() in 'aeiou':
            vogais+=l
    print(f'A palavra \033[32m{p}\033[m tem as vogais: \33[41m{vogais}\33[m')
'''
Palavras = ('Sabonete', 'Aroma', 'Chinelo', 'Porta retrato', 'Presente', 'Placa', 'Sacola')
for p in Palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(f'{l}',end='')

       