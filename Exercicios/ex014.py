'''
Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''
t = float(input('Informe a temperatura em ºC: '))
print('A temperatura de {:.1f}ºC correspende a {:.1f}ºF!'
#      .format(t, ((t*1.8000)+32.00)))
      .format(t, (((t*9)/5)+32)))
