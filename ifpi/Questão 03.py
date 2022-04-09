p = 0
#Questão 01
print('Como se chama o animal que faz "AU AU" em inglês?')
r = input().lower()

if r == 'dog':
    print('Certa resposta mais um ponto :)')
    p = p+1
else:
    print('Resposta Errada. :(')

#Questão 02
print('Como se fala gato em inglês?')
r = input().lower()

if r == 'cat':
    print('Certa resposta mais um ponto. :)')
    p = p + 1
else:
    print('Resposta Errada. :(')

#Questão 03
print('Como se chama mão em inglês?')
r = input().lower()

if r == 'hands':
    print('Certa resposta mais um ponto.:)')
    p = p + 1
else:
    print('Resposta Errada. :(')

#Questão 04
print('Como se chama carro em inglês?')
r = input().lower()

if r == 'car':
    print('Certa resposta mais um ponto.:)')
    p = p + 1
else:
    print('Resposta Errada. :(')


#Questão 05
print('Como se chama jogo em inglês?')
r = input().upper()

if r == 'game':
    print('Certa resposta mais um ponto.:)')
    p = p + 1
else:
    print('Resposta Errada. :(')


print(f'Seus pontos foram: {p}')