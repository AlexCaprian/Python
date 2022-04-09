print('''
Qual dos animais abaixo é um felino:
a) Porco.
b) Gata.
c) Lobo.
d) Vaca.
''')
r = input().lower()

if r == 'a':
    print('Errada')
elif r == 'b':
    print('Certa Resposta.')
elif r == 'c':
    print('Errada.')
elif r == 'd':
    print('Errada.')
else:
    print('Você não colocou nenhuma das alternativas.')