"""
Exercício Python 005.

Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e
seu antecessor.
"""

n = int(input('Digite um número: '))
print('O antecessor e sucessor de {0} são: {1} e {2}'.format(n, (n-1), (n+1)))
