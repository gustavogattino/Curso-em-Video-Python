'''
Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome "SANTO".
'''

cidade = input('Digite o nome de uma cidade: ')
print('O nome dessa cidade começa com a palavra "SANTO"? {}'.format('SANTO' in cidade.upper().split()[0]))
