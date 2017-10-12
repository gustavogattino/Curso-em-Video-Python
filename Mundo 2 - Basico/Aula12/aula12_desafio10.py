"""Aula 12 - Desafio 10."""

from random import randint
ppt = ['PEDRA', 'PAPEL', 'TESOURA']
print('Vamos jogar pedra, papel e tesoura! ', end='')
while True:
    comp = randint(0, 2)
    usua = int(input('Qual sua jogada?\n\n'
                     '1 - PEDRA  \n'
                     '2 - PAPEL  \n'
                     '3 - TESOURA \n'
                     '4 - SAIR \n\n'
                     '>>> '))-1

    if usua != 0 and usua != 1 and usua != 2 and usua != 3:
        print('Opção imválida...\n\n')
    else:
        if usua == 3:
            break
        elif comp == usua:
            print('Você escolheu {} e eu escolhi {}! \nEmpate!\n\n'
                  .format(ppt[usua], ppt[comp]))
        elif (comp == 0 and usua == 1
              or comp == 1 and comp == 2
              or comp == 2 and usua == 0):
            print('Você escolheu {0} e eu escolhi {1}! \n'
                  '{0} vence {1}... \033[32mVocê venceu\033[m.\n\n'
                  .format(ppt[usua], ppt[comp]))
        else:
            print('Você escolheu {0} e eu escolhi {1}! \n'
                  '{1} vence {0}... \033[31mEu venci\033[m.\n\n'
                  .format(ppt[usua], ppt[comp]))
