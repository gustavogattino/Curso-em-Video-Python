"""Aula 09 - Desafio 06."""

nome = input('Qual o seu nome completo? ')
print('O seu primeiro nome é {} e o seu último sobrenome é {}.'
      .format(nome.split()[0], nome.split()[len(nome.split())-1]))
