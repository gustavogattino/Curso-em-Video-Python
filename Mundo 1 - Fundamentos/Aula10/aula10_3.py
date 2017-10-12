"""Exemplos aula 10."""

n1 = float(input('Digite a primeiro nota: '))
n2 = float(input('Digite a segunda nota : '))
m = (n1 + n2) / 2
print('A sua média goi {:.1f}'.format(m))
# if m >= 7:
#    print('Sua média foi bom!')
# else:
#    print('Sua média foi ruim.')
print('Sua média foi boa!' if m >= 7 else 'Sua média foi ruim.')
