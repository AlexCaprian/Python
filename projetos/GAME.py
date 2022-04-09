from random import randint
print('Jogadas:\n[0] - PEDRA\n[1] - PAPEL\n[2] - TESOURA')
print('Escolha sua jogada:')
jogador = int(input())
itens = ('PEDRA', 'PAPEL', 'TESOURA')
CPU = randint(0, 1)
if jogador > 2:
    print('VALOR INVÁLIDO.')
else:
    print('*_*'*11)
    print(f'O jogador escolheu {itens[jogador]}.')
    print(f'A CPU escolheu {itens[CPU]}.')
    print('*_*'*11)

    if CPU == 0:
        if jogador == 0:
            print('EMPATE!!!')
        elif jogador == 1:
            print('JOGADOR VENCEU!!!')
        elif jogador == 2:
            print('JOGADOR PERDEU!!!')
    elif CPU == 1:
        if jogador == 0:
            print('JOGADO PERDEU!!!')
        elif jogador == 1:
            print('EMPATE!!!')
        elif jogador == 2:
            print('JOGADOR VENCEU!!!')
    elif CPU == 2:
        if jogador == 0:
            print('JOGADOR VENCEU!!!')
        elif jogador == 1:
            print('JOGADOR PERDEU!!!')
        elif jogador == 2:
            print('EMPATE!!!')