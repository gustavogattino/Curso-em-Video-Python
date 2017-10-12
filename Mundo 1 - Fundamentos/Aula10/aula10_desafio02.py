"""Aula 10 - Desafio 02."""

v = float(input('Você está dirigindo um carro. Qual velocidade ele está? '))
if v > 80:
    print('O limite de velocidade é 80km/h. Você foi multado em R${:.2f}!'
          .format((v-80)*7))
else:
    print('Tudo certo. Boa viagem!')
