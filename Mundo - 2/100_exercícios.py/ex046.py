'''
Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artificios, indo de 10 até 0,
com uma pausa de 1 segundo entre eles

Analise: 
For = Para fazer a contagem de 10 até 0;
modulo TIME a função SLEEP para fazer uma pausa de 1 seg;
Modulo Pygame para carregar imagem;

'''
#import pygame
from time import sleep
print('Contagem Regressiva')
for cont in range (10,-1,-1):
    print(cont)
    sleep(1)
print('BOOOMMM,BOOOMM,POOOMM')
'''
pygame.init()
l = 500
a = 450
j = pygame.display.set_mode((l,a))
i = pygame.image.load('C:\\Users\\Adamos\\Desktop\\ADAMOS\\CURSO_LP_PY\\Curso_em_video\\Mundo - 2\\Img\\fogos.gif')
j.blit(i,(0,0))
pygame.display.flip()
pygame.time.wait(2000)
pygame.quit()
'''