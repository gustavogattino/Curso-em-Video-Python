"""Aula 12 - Desafio 02."""

valor = int(input('Digite um número inteiro para conversão: '))
opcao = int(input('Qual a base de conversão?\n'
                  '1 - Binário '
                  '2 - Octal '
                  '3 - Hexadecimal\n'
                  '>>> '))
if opcao == 1:
    print('{} em binário é {}!'.format(valor, bin(valor)[2:]))
elif opcao == 2:
    print('{} em octal é {}!'.format(valor, oct(valor)[2:]))
else:
    print('{} em hexadecimal é {}!'.format(valor, hex(valor)[2:]))
