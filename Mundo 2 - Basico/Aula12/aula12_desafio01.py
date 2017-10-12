"""Aula 12 - Desafio 01."""

print('### Cálculo de financiamento mobiliário.\n')
vcasa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
anos = int(input('A casa será paga em quantos anos? '))
pres = vcasa / (anos * 12)

print('O valor da prestação mensal da casa será de R${:.2f}.'
      .format(pres))

if pres > (sal * 0.30):
    print('Desculpe. \033[31mSeu empréstimo foi negado\033[m. '
          'A prestação é muito alta para o seu orçamento.')
else:
    print('\033[32mEmpréstimo concedido\033[m! '
          'A prestação cabe no seu orçamento.'
          .format(pres, (sal * 0.30)))
