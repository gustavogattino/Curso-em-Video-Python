"""
Exercício Python 034.

Escreva um programa que pergunte o salário de um funcionário e calcule o valor
do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de
10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

sal = float(input('Qual o salário do funcionário? R$'))
if sal <= 1250:
    print('O seu salário de R${:.2f} será reajustado em 15%, '
          'totalizando R${:.2f}.'.format(sal, sal * 1.15))
else:
    print('O seu salário de R${:.2f} será reajustado em 10%, '
          'totalizando R${:.2f}.'.format(sal, sal * 1.10))
