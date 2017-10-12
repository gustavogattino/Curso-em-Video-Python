"""Aula 12 - Desafio 09."""

preco = float(input('Qual o valor do produto comprado? R$'))
op = int(input('\nQual a forma de pagamento?\n'
               '1 - À vista com dinheiro. (10% desconto)\n'
               '2 - À vista com cartão.   ( 5% desconto)\n'
               '3 - 2x no cartão.         (sem juros)\n'
               '4 - 3x ou mais no cartão. (20% juros)\n'
               '>>>> '))
if op == 1:
    print('O produto no valor de R${:.2f} sai por R${:.2f}.'
          .format(preco, (preco * 0.9)))
elif op == 2:
    print('O produto no valor de R${:.2f} sai por R${:.2f}.'
          .format(preco, (preco * 0.95)))
elif op == 3:
    print('O produto sai por 2 parcelas de R${:.2f} (R${:.2f}).'
          .format(preco/2, preco))
else:
    p = int(input('Quantas parcelas? '))
    print('O produto no valor de R${:.2f} sai por {} parcelas de R${:.2f} '
          '(R${}).'.format(preco, p, ((preco*1.3)/p), preco*1.3))
print('Volte sempre.')
