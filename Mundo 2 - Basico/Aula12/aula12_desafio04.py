"""Aula 12 - Desafio 04."""

from datetime import date
nasc = int(input('Qual o seu ano de nascimento (aaaa)? '))
idade = date.today().year - nasc
if idade < 18:
    print('É muito cedo pra você se alistar. '
          'Falta(m) {} ano(s) para o seu alistamento.'.format(18 - idade))
elif idade == 18:
    print('Esta na hora de se alistar!')
else:
    print('Você deveria ter se alistado a {} ano(s) atrás. '
          'Espero que você já esteja alistado.'.format(idade - 18))
