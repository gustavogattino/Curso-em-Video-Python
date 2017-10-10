'''
Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''
algo = input('Digite algo: ')
print('O tipo primitivo desse valor é {}.'.format(type(algo)))
print('Só tem espaços? {}'.format(algo.isspace()))
print('É um númerico? {}'.format(algo.isnumeric()))
print('É alfabético? {}'.format(algo.isalpha()))
print('É alfanumérico? {}'.format(algo.isalnum()))
print('Está em maiúsculas? {}'.format(algo.isupper()))
print('Está em minúsculas? {}'.format(algo.islower()))
print('Está captalizado? {}'.format(algo.istitle()))
