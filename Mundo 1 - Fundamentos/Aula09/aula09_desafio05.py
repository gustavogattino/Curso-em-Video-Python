"""Aula 09 - Desafio 05."""

frase = input('Digite uma frase: ')
print('Na frase inserida, a palavra "A" aparece {} vezes.\n'
      'Ela apareceu pela primeira vez na posição {}.\n'
      'Ela apareceu pela última vez na posição {}.'
      .format(frase.upper().count('A'), frase.upper().find('A'),
              frase.upper().rfind('A')))
