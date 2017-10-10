print('/'*20)
print('{:/^20}'.format('AULA 07'))
print('/'*20)

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('O resultado para as expressões aritiméticas entre {0} e {1} são:\n'
      'Soma {2}, produto {3}, divisão {4:.1f}'.format(n1, n2, s, m, d), end='')
print(', divisão inteira {0} e potência {1}.'.format(di, e))