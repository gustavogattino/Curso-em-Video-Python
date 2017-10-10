'''
Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''
from math import hypot
opo = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
#hip = (opo ** 2 + adj ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}.'.format(hypot(opo, adj)))