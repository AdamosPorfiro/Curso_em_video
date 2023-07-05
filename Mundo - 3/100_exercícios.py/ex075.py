'''
Crie um programa que tenha várias palavras(Não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
palavras = ('Sabonete', 'Sacola', 'Estojo', 'Porta retrato', 'Chinelo')
for p in palavras:
    vogais = ''
    for l in p:
        if l.lower() in 'aeiou':
            vogais+=l
    print(f'A palavra {p} tem as vogais {vogais}')