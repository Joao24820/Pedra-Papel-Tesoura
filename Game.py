from random import randint

itens = ('pedra', 'papel', 'tesoura')
comp = randint(0, 2)
print('[0] PEDRA\n[1] PAPEL\n[2] TESOURA')
print('Suas ações!! ')
jog = int(input('Qual é a sua jogada: '))
print('O computador escolheu: {} '.format(itens[comp]))
print('o jogador escolheu: {} '.format((jog)))

if comp == 0:
    if jog == 0:
        print('EMPATE')
    elif jog == 1:
        print('JOGADOR VENCEU')
    elif jog == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA !')

elif comp == 1:
    if jog == 0:
        print('COMPUTADOR VENCEU')
    elif jog == 1:
        print('EMPATE')
    elif jog == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVALIDA !!')

elif comp == 2:
    if jog == 0:
        print('O JOGADOR GANHOU ')
    elif jog == 1:
        print('COMPUTADOR GANHOU')
    elif jog == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA !!')
