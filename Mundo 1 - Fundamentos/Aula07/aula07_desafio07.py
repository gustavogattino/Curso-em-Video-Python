alt = float(input('Qual a altura em metros da parede?  '))
lar = float(input('Qual a largura em metros da parede? '))
print('Para pintar uma parede de {} metros de altura e {} metros de largura, '
      'totalizando uma área de {} metros quadrados, serão necessários {} litros de tinta.'
      .format(alt, lar, alt*lar, (alt*lar)/2))

