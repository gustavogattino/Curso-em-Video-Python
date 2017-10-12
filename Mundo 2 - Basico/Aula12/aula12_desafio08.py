"""Aula 12 - Desafio 08."""

print('### Calculo de IMC')
peso = float(input('Qual o seu peso (Kg?): '))
alt = float(input('Qual a sua altura (m) : '))
IMC = peso/(alt ** 2)
print('Seu IMC é {:.2f}! De acordo com a tabela de IMC, você está '
      .format(IMC), end='')
if IMC < 18.5:
    print('ABAIXO DO PESO.')
elif IMC >= 18.5 and IMC < 25:
    print('no peso IDEAL.')
elif IMC >= 25 and IMC < 30:
    print('com SOBREPESO.')
elif IMC >= 30 and IMC <= 40:
    print('OBESO.')
else:
    print('com OBESIDADE MÓRBIDA.')
