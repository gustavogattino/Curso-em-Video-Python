"""Aula 07 - Desafio 06."""

print('/' * 30)
print('{:/^30}'.format('CONVERSOR DE BRL USD'))
print('/' * 30, '\n')
d = float(input('Digite o valor em BRL: R$ '))
print('Seus R${0} reais valem U${1:.2f} Dólares.'.format(d, d/3.27))
