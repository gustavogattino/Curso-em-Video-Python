'''
Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados
'''

n = input('Digite um número de 0000 à 9999: ').zfill(4)
print('Unidade: {}\nDezena : {}\nCentena: {}\nMilhar : {}'.format(n[3],n[2],n[1],n[0]))