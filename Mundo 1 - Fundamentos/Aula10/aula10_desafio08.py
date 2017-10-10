l1 = float(input('Digite o tamanho da primeira reta: '))
l2 = float(input('Digite o tamanho da segunda reta : '))
l3 = float(input('Digite o tamanho da terceira reta: '))

if (l1 + l2) < l3:
    print('Estas retas não podem formar um triângulo.')
else:
    if (l1 + l3) < l2:
        print('Estas retas não podem formar um triângulo.')
    else:
        if (l2 + l3) < l1:
            print('Estas retas não podem formar um triângulo.')
        else:
            print('As retas podem formar um triângulo.')
