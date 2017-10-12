"""Aula 09 - Desafio 01."""

nome = input('Digite seu nome completo: ')
print('Seu nome e sobrenome com todas as letras em maiúsculo fica: {}'
      .format(nome.upper()))
print('Seu nome e sobrenome com todas as letras em minúsculo fica: {}'
      .format(nome.lower()))
print('Seu nome e sobrenome tem {} letras.'.format(len(nome.replace(" ", ""))))
print('Seu nome tem {} letras'.format(len(nome.split()[0])))
