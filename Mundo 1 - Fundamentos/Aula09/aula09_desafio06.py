'''
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o ultimo nome separadamente.
'''

nome = input('Qual o seu nome completo? ')
print('O seu primeiro nome é {} e o seu último sobrenome é {}.'
      .format(nome.split()[0], nome.split()[len(nome.split())-1]))
