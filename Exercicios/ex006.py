"""
Exercício Python 006.

Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz
quadrada.
"""

n = int(input('Digite um valor: '))
print('O dobro de {0} vale {1}.\n'
      'O triplo de {0} vale {2}.\n'
      'A raiz quadrada de {0} vale {3:.2f}.'
      .format(n, (n*2), (n*3), (n**(1/2))))
