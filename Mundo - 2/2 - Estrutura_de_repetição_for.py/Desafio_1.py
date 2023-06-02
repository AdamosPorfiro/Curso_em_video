'''
Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artificios, indo de 10 até 0,
com uma pausa de 1 segundo entre eles

Analise: 
For = Para fazer a contagem de 10 até 0;
modulo TIME a função SLEEP para fazer uma pausa de 1 seg;
Modulo Pygame para carregar imagem;

'''
#import pygame
print('\n'+'{:^10}'.format('Contador regressiva'))
from time import sleep
for c in range(10,-1,-1):
    print(c)
    sleep(1)
print('BOOOMMM! POOOOMMM!')

'''Vamos carregar uma imagem usando pygame
pygame.init() # Init vai Inicializamos pygame;
l = 500 # Definimos uma largura;
a = 450 # Definimos uma Altura;
j = pygame.display.set_mode((l, a)) # Display que vai ser a janela onde a imagem será exibida;
im = pygame.image.load('C:\\Users\\Adamos\\Desktop\\ADAMOS\\CURSO_LP_PY\\Curso_em_video\\Mundo - 2\\Img\\fogos.gif') # Load vai carregamos a imagem;
j.blit(im, (0,0)) # Blit vai exibir nossa janela na posição 0,0;
pygame.display.flip() # Flip vai atualizar a janela uma vez;
pygame.time.wait(2000) # time.wait vai deixar a janela em exibição por 2 segundos ;
pygame.quit() # Vai fechar a janela e reiniciar o programa;'''


