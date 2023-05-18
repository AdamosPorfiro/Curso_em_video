'''
===== Desafio 7 =====

Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.

Metodo dos 5 Q's

1 - Quais são os dados de entrada?
-> imort biblioteca playsound
-> input arquivo_mp3

2 - O que devo fazer com esses dados?
-> Abrir e reproduzir um aúdio de um arquivo mp3

3 - Quais são as restrições do programa?
-> Usando biblioteca playsound
-> Arquivos mp3

4 - Qual o resultado esperado?
-> Abrir e reproduzir um aúdio de arquivo mp3

5 - Quais são os passos para se alcançar o resultado?
#1 Importar o biblioteca playsound e a função playsound
#2 Cria uma variavel com o caminho do arquivo Ex.:Caminho = \\file\\caminho
#3 Chama função playsound(Caminho)


'''
print('Reprodução aúdio - Righteous Brothers-Unchained Melody.mp3')
from playsound import playsound
caminho_arquivo = 'C:\\Users\\Ideal\\Documents\\GitHub\\Curso_em_video\\mp3\\Righteous Brothers-Unchained Melody.mp3'
playsound(caminho_arquivo)
