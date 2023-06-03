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
        from unidecode import unidecode
    1 - input frase .split().strip()
    2 - frase = unidecode(''.join(frase))
    3 - for c in (len(frase)):
    4 - if s[0::].find(frase) == s[::-1].find(frase)
    5 -     print('PARABENS, essa é um palindromo!')
    6 -     break
    7 - else:
    8 -     print QUE PENA! Essa frase não é um palindromo
    

    # TESTE  - 1
frase = 'nãosei'

if frase[0::].find(frase) == frase[::-1].find(frase):
    print('É um palindromo')
else:
    print('Não é um palindromo')  

else:
    print('Não é um palindromo')

   # TESTE - 2 
#Vai tirar todos os espaços e acentos
from unidecode import unidecode
f = str(input('Digite um palindromo: ')).strip().split()
f = unidecode(''.join(f)).lower()
#Vamos criar a condição
if f == f[::-1]:
        print('PARABÉNS, é um palindromo!') 
else:
    print('OPS! Não é um palindromo!')
'''
'''
print('{:=^30}''\n{:^4}Detector de palindromo''\n{:=^30}'.format('',' ',''))
from unidecode import unidecode # Modulo e função que tira acentuação das palavras;
f = str(input('{:^5}Digite um palindromo\n\n'.format(' '))).strip().lower().split() # Receber input sem espaços da direita e esquerda e c/ palavras separadas
f = unidecode(''.join(f)) # Aplicar a função que foi importada e juntar as palavras que foram splitadas, removendo os espaços entre elas e por fim, deixar tudo minusculo
palindromo = True # Definimos uma variavel como verdadeira
for c in range(len(f)//2): # Usamos for para ler frase e dividir a quantidade de caracteres por 2
       if f[c] != f[-c-1]: # Se os caracteres de f forem iguais os ultimos caracteres de f, então
              palindromo = False # Variavel palindromo será falsa
              break # Pare
if palindromo: # Caso a condição de for seja correspondida a variavel palindromo que iniciamos como true sera false e caos contrario ela continua true
       print('PARABÉNS, é um palindromo!\n') 
else:
       print('OPS! Não é um palindromo!\n')
'''

f = str(input('Digite uma frase: ')).strip().upper()
palavras = f.split()
juntou = ''.join(palavras)
inverso = juntou[::-1]
'''for letra in range(len(juntou)-1, -1, -1):
    inverso += juntou[letra]
if inverso == juntou:
    print('Sim, é um palindromo\nA frase {} lida de trás pra frente é {}'.format(juntou, inverso))
else:
    print('Não é um palindromo')'''
if inverso == juntou:
    print('Sim, é um palindromo\nA frase {} lida de trás pra frente é {}'.format(juntou, inverso))
else:
    print('Não é um palindromo')