'''
Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de
tinta pinta uma área de 2 metros quadrados.
'''
lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
a = lar * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\n'
      'Para pintar esse parede, você precisará de {}lt de tinta.'
      .format(lar, alt, a, (a/2)))