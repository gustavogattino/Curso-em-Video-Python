nome = str(input('Qual o seu nome? ')).strip()
if nome.upper() == 'GUSTAVO':
    print('Seu nome é muito lindo.')
else:
    print('Que nome normal você tem.')
print('Bom dia, {}'.format(nome))