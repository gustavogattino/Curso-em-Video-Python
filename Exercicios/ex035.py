'''
Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
'''
l1 = float(input('Digite o comprimento da primeira reta: '))
l2 = float(input('Digite o comprimento da segunda reta : '))
l3 = float(input('Digite o comprimento da terceira reta: '))

if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
    print('Estas retas não podem formar um triângulo!')
else:
    print('Estas retas podem formar um triângulo!')
