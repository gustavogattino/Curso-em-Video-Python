"""Aula 12 - Desafio 06."""
from datetime import date
nasc = int(input('Qual o ano em que você nasceu (aaaa)? '))
idade = date.today().year - nasc
print('De acordo com a Confederação Nacional de Natação, sua categoria é a ',
      end='')
if idade <= 9:
    print('MIRIM.')
elif idade > 9 and idade <= 14:
    print('INFANTIL.')
elif idade > 14 and idade <= 19:
    print('JUNIOR.')
elif idade == 20:
    print('SÊNIOR.')
else:
    print('MASTER.')
