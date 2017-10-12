"""Aula 10 - Desafio 01."""

from random import randint
c = randint(0, 5)
print('O computador escolheu um número aleatório de 0 à 5. '
      'Você consegue adivinhar qual foi?')
p = int(input('Qual número você acha que ele escolheu? '))
if p > 5:
    print('{} é um número muito alto! O computador só escolhe entre 0 e 5.'
          .format(p))
if p < 0:
    print('{} é um número muito baixo! O computador só escolhe entre 0 e 5.'
          .format(p))
if p == c:
    print('ACERTOU MIZERAVI! O computador escolheu {} e você acertou!'
          .format(c))
else:
    print('Errou! O computador escolheu {} e você escolheu {}.'.format(c, p))
