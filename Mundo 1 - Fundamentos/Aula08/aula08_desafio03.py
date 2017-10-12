"""Aula 08 - Desafio 03."""

import math
ang = int(input('Insira um ângulo qualquer: '))
sen = math.sin(ang)
cos = math.cos(ang)
tan = math.tan(ang)

print('Para {}, temos um seno de {}, um cosseno de {} e uma tangente de {}'
      .format(ang, sen, cos, tan))
