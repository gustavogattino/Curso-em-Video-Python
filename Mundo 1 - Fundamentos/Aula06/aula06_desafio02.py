"""Aula 06 - Desafio 02."""

algo = input('Digite alguma coisa: ')
print('{} é numero? {}'.format(algo, algo.isnumeric()))
print('{} é letra? {}'.format(algo, algo.isalpha()))
print('{} é numeros e/ou letras? {}'.format(algo, algo.isalnum()))
print('{} está apenas com letras minúsculas? {}'.format(algo, algo.islower()))
print('{} está apenas com letras maiúsculas? {}'.format(algo, algo.isupper()))
print('{} contém apenas números? {}'.format(algo, algo.isdigit()))
