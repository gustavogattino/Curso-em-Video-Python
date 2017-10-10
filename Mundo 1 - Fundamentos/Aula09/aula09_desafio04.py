'''
Crie um programa que leia o nome de uma pessoa
e diga se ela tem "SILVA" no nome.
'''

nome = input('Digite seu nome: ')
print('O nome inserido possui o sobrenome "SILVA"? {}'.format('SILVA' in nome.upper()))
