"""Aula 12 - Desafio 05."""

n1 = float(input('Qual a primeira nota do aluno? '))
n2 = float(input('Qual a segunda nota do aluno?  '))
media = (n1 + n2)/2
if media < 5:
    print('Sua média foi \033[31m{}\033[m. '
          'Você está \033[31mREPROVADO\033[m.'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média foi \033[33m{}\033[m. '
          'Você está em \033[33mRECUPERAÇÃO\033[m.'.format(media))
else:
    print('Sua média foi \033[32m{}\033[m. '
          'Você está \033[32mAPROVADO\033[m.\n'
          'Boas férias.'.format(media))
