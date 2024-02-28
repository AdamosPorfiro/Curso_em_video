"""
Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artificios, 
indo de 10 até 0, com uma pausa de 1 segundo entre eles

"""

from time import sleep
from PIL import Image

for c in range(10,-1,-1): #Vai fazer a contagem tirando 1
    print(c)
    sleep(1)

# Carrego a imagem
imagem = Image.open("C:\\Users\\Ideal\\Documents\\GitHub\\Curso_em_video\\Curso_em_video\\Mundo - 2\\2 - Estrutura_de_repetição_for.py\\fogos_.gif")
#Abre a imagem
imagem.show()

