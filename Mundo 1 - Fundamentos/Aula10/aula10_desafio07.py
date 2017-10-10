salario = float(input('Qual o salário do funcionário? '))
if salario <= 1250:
    print('O novo salário do funcionário é R${:.2f}.'.format(salario * 1.15))
else:
    print('O novo salário do funcionário é R${:.2f}.'.format(salario * 1.10))
