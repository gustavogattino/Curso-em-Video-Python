'''
Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
'''
cidade = str(input('Qual cidade você nasceu? ')).strip()
print('A cidade que você nasceu possui "SANTO" no nome? {}'.format('SANTO' in cidade.upper().split()[0]))