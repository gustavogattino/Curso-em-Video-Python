'''
Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
'''
n = int(input('Digite um número para ver sua tabuada: '))
print('-'*14)
print('{0:2} x  1 = {1:3}\n'
      '{0:2} x  2 = {2:3}\n'
      '{0:2} x  3 = {3:3}\n'
      '{0:2} x  4 = {4:3}\n'
      '{0:2} x  5 = {5:3}\n'
      '{0:2} x  6 = {6:3}\n'
      '{0:2} x  7 = {7:3}\n'
      '{0:2} x  8 = {8:3}\n'
      '{0:2} x  9 = {9:3}\n'
      '{0:2} x 10 = {10:3}'
      .format(n, (n*1), (n*2), (n*3), (n*4), (n*5), (n*6), (n*7), (n*8), (n*9), (n*10)))
print('-'*14)
