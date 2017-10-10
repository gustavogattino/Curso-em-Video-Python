n = int(input('Insira o valor par calcular a tabuada: '))
print('O valor da tabuada de {0} é:\n'
      '1 - {1:^4} 2 - {2:^4} 3 - {3:^4}\n'
      '4 - {4:^4} 5 - {5:^4} 6 - {6:^4}\n'
      '7 - {7:^4} 8 - {8:^4} 9 - {9:^4}'
      .format(n, n * 1, n * 2, n * 3, n * 4, n * 5, n * 6, n * 7, n * 8, n * 9))
