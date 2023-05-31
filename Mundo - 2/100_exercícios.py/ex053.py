'''
Crie um programa que leia um frase qualquer e diga se ela é um palindromo. Desconsiderando os espaços e acentos.

Palindromo são palavras ou frases que podem ser lidar do começo pro fim ou do fim pro começo;

Ex: Apos a sopa, A sacada da casa, A torre da derrota, O lobo ama o bolo, Anotaram a data da maratona.

Outra forma de identificar um palindromo é verificando apenas a metade do caminho: 
Ex.: Radar = 'ra' e 'ra' Apos a sopa = 'apos' 'sopa' 

Fazemos a divisão inteira por 2 do indice da string Ex.: Desconsiderando os espaços e acentos:
Após a sopa = 8 caracteres // 2 = 4 caracteres, então será verificado 4 caracter dessa frase.

Analisar: Para que possamos tirar os acentos de uma frase, e converte-las em seus respectivos caracteres, usamos 
o modulo UNIDECODE função UNIDECODE - pip install unidecode[]

Para desconsiderarmos os espaços da frase, vamos splitar a frase e em seguida vamos junta-lá novamente usando as funções:
SPLIT() -> Separar cada palavra
STRIP() - Tirar espaços da esq. e dir
JOIN() -> Juntar todas as palavra

Para criar a condição certa usaremos:
FOR com um find que vai ler a frase de frente pra trás e de trás pra frente

Quais são os dados de entrada?
input frase

O que eu devo fazer com esses dados?
Devo exibir na tela se a frase é um palindromo ou não!

Quais são as restrições desse problema?
A frase deve ser um palindromo ou não

Qual é o resultado esperado?
Exibir se a frase informada é um palindromo ou não

Quais são os passos para se alcançar o resultado esperado?
    1 - from unidecode import unidecode
    2 - input frase .split().strip()
    3 - frase = unidecode(''.join(frase)).lower()
    4 - if s[0::] == s[::-1]
    5 -     print('PARABENS, essa é um palindromo!')
    5 - else:
    7 -     print QUE PENA! Essa frase não é um palindromo
'''
from unidecode import unidecode
f = str(input('Digite um palindromo: ')).strip().split()
f = unidecode(''.join(f)).lower()
p = True
for c in range(len(f)//2):
    if f[c] != f[-c-1]:
        p = False
        break
if p:
    print('Sim é um palindromo!')
else:
    print('Não é um palindromo!')


