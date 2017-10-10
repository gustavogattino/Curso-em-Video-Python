'''
Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se
o usuário venceu ou perdeu.
'''
from random import randint
from time import sleep
comp = randint(1, 10)
print('Eu vou pensar em um número de 1 a 10. Tente adivinhar que número é esse.')
num = int(input('Eu pensei no número... '))
print('\nprocessando...\n')
sleep(2)
if comp == num:
    print('Você ganhou! Eu realmente estava pensando no {}.'.format(num))
else:
    print('Ganhei! Eu estava pensando {} e não {}.'.format(comp, num))
