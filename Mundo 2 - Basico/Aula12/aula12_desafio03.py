"""Aula 12 - Desafio 03."""

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

if n1 > n2:
    print('{} é maior que {}!'.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}!'.format(n2, n1))
else:
    print('Os valores são iguais.')
