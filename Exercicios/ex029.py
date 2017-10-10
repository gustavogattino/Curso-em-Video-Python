'''
Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''
vel = float(input('Você está viajando de carro. A qual velocidade o carro está andando? '))
if vel > 80:
    print('Você foi multado! A velocidade máxima da via é 80km/h!\n'
          'O valor a pagar pela multa é R${:.2f}!'.format((vel - 80) * 7))
else:
    print('Tudo certo! Boa viagem.')