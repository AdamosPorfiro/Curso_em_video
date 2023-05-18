"""
Oque é uma cadeia de caracteres?
É qualquer frase produzida, muito comumente chamada de "String" cadeia de texto.

Para o python toda cadeia de texto está entre aspas simples ' ou duplas ".

Quando criamos uma variavel Ex.: Frase = Curso em video python
O python reserva na memoria do computador um espaço para cada letra e espaço dessa frase
Ex.: C = 1, u = 2, r = 3, s = 4, o = 5. Para cada letra um espaço reservado incluindo os espaços entre as frases tambem.   

Tecnica de fatiamente: É conseguir pegar pedaços de uma frase e tratar ela.
frase = 'Adamos'
print (frase[2])
O programa vai imprimir para o usuario o indice 2 da variavel frase, sendo assim a letra "a" minuscula;

outro exemplo de fatiamente:
frase = 'Adamos'
print(frase[2:5]) Ele vai imprimir na tela do 2 ao 5 excluindo o 5, ou seja de 2 ao 4.

trabalhar com fatiamento ele remove o ultimo indice

outro exemplo de fatiamento:
frase= 'Adamos'
print(frase[0:5:2]) Ele exibi na tela a frase pulando 2 letras e imprimindo a 2° 

outro exemplo:
frase='Adamos Porfiro'
print(frase[:6]) Ele exibi na tela os 6 primeiros caracteres, já que antes dos dois pontos, não temos nenhum outro inicio

outro exemplo:
frase= 'Adamos Porfiro'
print(frase[6:]) Aqui ele exibi na tela a partir do caracter 6 todos os outros caracteres, já que ele apresenta um inicio, mas não um fim;

outro exemplo:
frase='Adamos Porfiro'
print (frase[2::3]) Ele vai começar do caracter 2 e pular de 3 em 3 exibindo o 3 caracter até chegar o fim da lista, caso chegue ao fim e não exista
um 3 caractere ele não exibira mais.

[] = Python reconhece o conchete como uma estrutura de dados que é chamada de lista;

Formas de analisar um string:
len = significa comprimento, que vai dizer pra gente o comprimento de uma frase
count = Contador, exemplo de uso frase = 'Adamos' print(frase.count('a')) O count vai contar quantas vezes apareçe a letra a minuscula.
outro exemplo de count é print(frase.count('a',0,8)) Ele vai verificar quantas vezes a letra "a" apareçe na frase contanto do indice 0 a 7 
find = Econtrar, Ex.: Print(frase('amos')) Ele vai indicar em que indice 'amos' começa veja no code lá em baixo.
in = Podemos dizer adamos in frase. frase = 'Adamos Porfiro' print('Adamos' in frase)

Formas de fazer transformações em string:
replace = reposicionar, trocar. Ex.: frase.replace('Adamos', 'Jordam') ele vai fazer a troca do nome Adamos por Jordam
upper() = Significa pra cima. frase.upper() Ele vai tornar a frase em maiuscula
lower() = Significa pra baixo, o contrario de upper
capitalize() = Vai jogar todos os caracteres para minusculos e apenas os primeiros caracter da frase será maiuscula;
title() = Vai tornar o primeiro caractere de cada palavra maiuscula
strip() = Vai remover todos os espaços inuteis no inicio e no fim da string
rstrip() = right - Vai remover apenas os espaços inuteis da direita
lstrip() = left - Vai remover apenas os espaços inuteis da esquerda

Formas de dividir um string:
split() = Cria uma divisão usando os espaços da string, refazendo os indices. Logo se uma frase possui 6 palavras, cada palavra irá possuir
o seu proprio indice

Formas de fazer junção em uma string:
join = Vai juntar as palavras da string Ex.: '-'.join(frase) Ele vai usar o tracinho para juntar novamente as palavras que foram splitadas

"""

frase = "  Adamos Porfiro  "
print(frase[8])  # o
print(frase[1:8])  # damos P
print(frase[0:13:2])  # Exibi "A" conta 2 e exibi o 2 "a" "o" " " "o" " f " "r" Aao ofr
print(frase[:6])  # Adamos
print(frase[6:])  # Porfiro
print(frase[0::2])  # Aao ofr
print(len(frase))  # 14 caracteres
print(frase.count("a"))  # Apareçe 1 vez apenas.
print(frase.count("a", 0, 14))  # Apareçe 1 vez apenas.
print(frase.find("amo"))  # Resultado é 2, já que 0=A 1=d 2=a, logo inidice 2 começa a palavra indicada amos.
print("Adamos" in frase)  # Se a palavra Adamos existe na variavel frase, se sim ele vai retornar um valor booleano, true no caso.
print(frase.replace("Adamos", "Jordam"))  # Troca nome Adamos por Jordam
print(frase.upper())  # Torna tudo maisculo e inclusive mantem as que já estavam caixa alta, altas.
print(frase.lower())  # Torna tudo minusculo, inclusive as que estavam com caixa alta.
print(frase.capitalize())  # Todas viram minusculas e apenas as primeiras letras de toda a frase fica maiuscula.
print(frase.title())  # Nesse caso ele vai pegar o primeiro caractere de cada palavra e deixar maiusculo, o restante minusculo, como um titulo.
print(frase.strip()) # Remove todos os espaços inuteis no inicio e fim da string.
print(frase.rstrip()) # Remove espaços da direita
print(frase.lstrip()) # Remove espaços da esquerda
print(frase.split()) # Ele dividi as palavras, Adamos se torna independente e porfirio tambem, gerando assim um lista de uma cadeia de caracteres
print(frase.split('-'.join(frase))) 
print('-'.join(frase)) # Vai juntar a frase usando - tracinho, se usarmos em uma frase splitada ele vai juntar ela novamente, como no exemplo acima
texto = ''' Em linguística, a noção de texto é ampla e ainda aberta a uma definição mais precisa. 
Grosso modo, pode ser entendido como manifestação linguística das ideias de um autor, 
que serão interpretadas pelo leitor de acordo com seus conhecimentos linguísticos e culturais.
Seu tamanho é variável. '''
print(len(texto))
print(texto.count('a'))
print(len(texto.strip()))


