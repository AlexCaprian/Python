from random import randint
from time import sleep
def escolha(resposta):
        if resposta == 's':
            print('Vamos nessa...')
            sleep(0.5)
        elif resposta == 'n':
            print('Ok...\nTchauuu...')
            return True
continuar = False
#Fazer um loop infinito.
while not continuar:
    pc = randint(0, 10)
    print('Você quer jogar? Escreva: Sim ou Não.')
    e = input().strip().lower()[0]
    if e == 'n':
        print('Pois ok, tchauuu...')
        None
    elif e == 's':
        #A pergunta para escolher o número.
        print('Ebaaa\nEntão vamos lá\nAcabei de pensar em um número de 0 a 10...')
        acerto = False
        cont = 0
        while not acerto:
            jogada = int(input())
            cont += 1
            if jogada == pc:
                if cont == 1:
                    print(f'Você acertou de primeira, teve muita sorte.')
                    sleep(0.5)
                    print('Você quer jogar novamente?\nSim ou Não...')
                    resposta = str(input()).strip().lower()[0]
                    continuar = escolha(resposta)
                elif cont > 2 or cont < 5:
                    print(f'Você acertou em apenas {cont}, muito bem.')
                    sleep(0.5)
                    print('Você quer jogar novamente?\nSim ou Não...')
                    resposta = str(input()).strip().lower()[0]
                    continuar = escolha(resposta)
                elif cont > 5:
                    print(f'Você acertou com mais de {cont} tentativas, você consegue melhorar.')
                    sleep(0.5)
                    print('Você quer tentar de novo?\nSim ou Não...')
                    resposta = str(input()).strip().lower()[0]
                    continuar = escolha(resposta)
            else:
                if jogada < pc:
                    print('Mais... Tente novamente.')
                elif jogada > pc:
                    print('Menos... Tente novamente.')
    elif e not in 'sn':
        print(f'Você digitou o valor errado...\nTCHAU')
        print('@#!$' * 100000)