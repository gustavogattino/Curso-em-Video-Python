"""
Exercício Python 018.

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.
"""

from math import radians, sin, cos, tan
ang = radians(float(input('Digite o ângulo que você deseja: ')))
print('O ângulo de {0} tem o SENO de {1:.2f}\n'
      'O ângulo de {0} tem o COSSENO de {2:.2f}\n'
      'O ângulo de {0} tem a TANGENTE de {3:.2f}'
      .format(ang, sin(ang), cos(ang), tan(ang)))
