"""Exemplos aula 11."""

print('\033[7;30;mOlá, Mundo!\033[m')

o = 'Olá'
m = 'Mundo'

print('{}{}{}, {}{}{}!'
      .format('\033[31;47m', o, '\033[m', '\033[4;33;42m', m, '\033[m'))
cores = {'limpa': '\033[m',
         'azul': '\033[1;30;46m',
         'vermelho': '\033[4;30;41m'}
print('{1}{2}{0}, {3}{4}{0}!'
      .format(cores['limpa'], cores['azul'], o, cores['vermelho'], m))
