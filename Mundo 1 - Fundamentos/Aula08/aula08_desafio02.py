from math import hypot
op = float(input('Digite o comprimento do cateto oposto de um triangulo retangulo: '))
ad = float(input('Digite o comprimento do cateto adjacente do triangulo retangulo: '))
hip = hypot(op, ad)

print('O valor da hipotenusa deste triangulo retangulo é {}'.format(hip))
