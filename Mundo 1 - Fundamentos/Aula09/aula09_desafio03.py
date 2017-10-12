"""Aula 09 - Desafio 03."""

cidade = input('Digite o nome de uma cidade: ')
print('O nome dessa cidade começa com a palavra "SANTO"? {}'
      .format('SANTO' in cidade.upper().split()[0]))
