"""Aula 10 - Desafio 03."""

n = int(input('Digite um número: '))
if n == 0:
    print('Zero não é par nem ímpar! Ou é?')
else:
    print('Este número é par!' if (n % 2) == 0 else 'Este número é impar.')
