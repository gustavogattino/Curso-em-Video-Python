'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas;
- O nome com todas minúsculas;
- Quantas letras ao todo (sem considerar espaços);
- Quantas letras tem o primeiro nome.
'''

nome = input('Digite seu nome completo: ')
print('Seu nome e sobrenome com todas as letras em maiúsculo fica: {}'.format(nome.upper()))
print('Seu nome e sobrenome com todas as letras em minúsculo fica: {}'.format(nome.lower()))
print('Seu nome e sobrenome tem {} letras.'.format(len(nome.replace(" ",""))))
print('Seu nome tem {} letras'.format(len(nome.split()[0])))
