'''
Crie um programa que tenha várias palavras(Não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = ('Adamos', 'Garrafa', 'Galinha', 'Macarrão', 'Batata', 'Bacia', 'Quadro', 'Fotos', 'Jargões', 'Peido', 'Video')

for palavras in palavras: #For para entrar na tupla
    letras_concatenadas = '' #Variavel que vai armazenar cada palavra
    for letra in palavras: #Outro for para entrar em cada palavra da tupla e separar as letras
        if letra in 'AEIOUaeiou': #Vamos achar as vogais
            letras_concatenadas += letra + ' ' #Se tiver vogais vamos colocar essas vogais dentro da variavel que criamos
    print(f"{palavras}: {letras_concatenadas}") #Vamos printar cada palavra e cada vogal correspondente  dentro de cada palavra
        
    
       