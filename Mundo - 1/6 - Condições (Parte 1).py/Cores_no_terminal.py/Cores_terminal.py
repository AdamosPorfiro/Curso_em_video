'''
Código ANSI - Escape sequence

Começa com uma sequencia usando \033[style; text; back m]

style = Estilo da fonte;
Texte = Cor do texto;
Back = Cor do fundo;

Ex: \033[0:33:44m

Códigos para estilo que funcionam melhor com python:
0 - none
1 - bold
4 - underline
7 - negative

Código de cores para texto:
30 - Branco;
31 - Vermelho;
32 - Verde;
33 - Amarelo;
34 - Azul;
35 - Roxo;
36 - Azul esmeralda;
37 - Cinza;

Código de background:
40 - Branco;
41 - Vermelho;
42 - Verde;
43 - Amarelo;
44 - Azul;
45 - Roxo;
46 - Azul esmeralda;
47 - Cinza;

logo \033[0:33:44m - none para estilo, cor: Amarelo, cor de fundo: Azul;
'''

#Utilizando cores em python;

print("\33[0;33;40mTeste\33[m")

print('\033[1;32;41mOlá, mundo!\033[m')
a = 'Adamos'
cores = {'Limpa': '\033[m', 
         'azul': '\033[m', 
         'amarelo': '\033[M', 
         'pretoebranco': '\033[7;30m'
         }
print('Olá, {}{}!!!{}'.format(cores['pretoebranco'], a, cores['Limpa']))

