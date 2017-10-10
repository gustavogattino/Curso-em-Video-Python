dis = float(input('Qual a distância da sua viagem em Kms? '))
if dis <= 200:
    print('Para viagens de até 200km, o preço da passagem é R$0,50 por Km.')
    print('Sua passagem vai custar R${:.2f}.'.format(dis*0.50))
else:
    print('Para viagens acima de 200km, o preço da passagem é R$0,45 por Km.')
    print('Sua passagem vai custar R${:.2f}.'.format(dis*0.45))
print('Boa viagem!')
