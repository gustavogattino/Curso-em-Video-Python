"""Aula 08 - Desafio 05."""

from random import sample
al1 = input('Aluno 1: ')
al2 = input('Aluno 2: ')
al3 = input('Aluno 3: ')
al4 = input('Aluno 4: ')
print('A ordem de apresentação será {}!'
      .format(sample([al1, al2, al3, al4], 4)))
