"""Aula 12 - Desafio 07."""

l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))
if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
    print('Estas retas não podem formar um triângulo.')
else:
    print('Estas retas formam um triângulo!\n'
          'Este triângulo é ', end='')
    if l1 == l2 and l2 == l3:
        print('Equilátero!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Isósceles!')
    else:
        print('Escaleno!')
