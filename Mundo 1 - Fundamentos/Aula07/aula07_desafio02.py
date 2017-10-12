"""Aula 07 - Desafio 02."""

n = int(input('Insira o valor: '))
print('O valor inserido foi {0}. '
      'Seu dobro é {1}, '
      'seu triplo é {2} '
      'e sua raiz quadrada é {3}.'
      .format(n, n * 2, n * 3, int(n ** (1/2))))
