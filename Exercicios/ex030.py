"""
Exercício Python 030.

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou
ÍMPAR.
"""

num = int(input('Insira um número inteiro qualquer: '))
if num == 0:
    print('ZERO não é um número PAR, nem ÍMPAR!\n(Ou é?)')
else:
    print('{} é um número PAR!'.format(num) if num % 2 == 0
          else '{} é um número ÍMPAR!'.format(num))
