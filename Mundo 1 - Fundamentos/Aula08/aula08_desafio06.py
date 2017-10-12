"""Aula 08 - Desafio 06."""

from pygame import mixer
mixer.init()
mixer.music.load('D:\Music\AAAAA.mp3')
mixer.music.play()
para = input('aperte enter para parar.')
