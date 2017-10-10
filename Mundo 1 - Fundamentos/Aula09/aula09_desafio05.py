'''
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A";
- Em que posição ela aparece pela primeira vez;
- Em que posição ela aparece a última vez.
'''

frase = input('Digite uma frase: ')
print('Na frase inserida, a palavra "A" aparece {} vezes.\n'
      'Ela apareceu pela primeira vez na posição {}.\n'
      'Ela apareceu pela última vez na posição {}.'
      .format(frase.upper().count('A'),frase.upper().find('A'), frase.upper().rfind('A')))
