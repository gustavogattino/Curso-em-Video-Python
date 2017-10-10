n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais outro número: '))
if n1 > n2:
    maior = n1
else:
    maior = n2
if maior < n3:
    maior = n3
print('O maior número é {}.'.format(maior))
if n1 < n2:
    menor = n1
else:
    menor = n2
if menor > n3:
    menor = n3
else:
    print('O menor número é {}.'.format(menor))
