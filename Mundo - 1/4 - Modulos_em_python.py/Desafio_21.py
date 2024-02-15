"""
Desafio 21
Faça um programa em python que abra e reproduza o audio de um arquivo MP3

"""
from pygame import init, mixer
from time import sleep

init() # Incia o pygame
caminho_arquivo = "C:\\Users\\Ideal\\Documents\\GitHub\\Curso_em_video\\Curso_em_video\\Mundo - 1\\4 - Modulos_em_python.py\\Musica.mp3"
mixer.music.load(caminho_arquivo) #Mixer possui 
mixer.music.play()
sleep(5)