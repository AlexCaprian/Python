dia = int(input())
mes = int(input())

if dia >= 21 and dia <= 31 and mes == 3 or dia >= 1 and dia <= 19 and mes == 4:
    print('Áries')
elif dia >= 20 and dia <= 30 and mes == 4 or dia >= 1 and dia <= 20 and mes == 5:
    print('Touro')
elif dia >= 21 and dia <= 31 and mes == 5 or dia >= 1 and dia <= 21 and mes == 6:
    print('Gêmeos')
elif dia >= 22 and dia <= 30 and mes == 6 or dia >= 1 and dia <= 22 and mes == 7:
    print('Câncer')
elif dia >= 23 and dia <= 31 and mes == 7 or dia >= 1 and dia <= 22 and mes == 8:
    print('Leão')
elif dia >= 23 and dia <= 31 and mes == 8 or dia >= 1 and dia <= 22 and mes == 9:
    print('Virgem')
elif dia >= 23 and dia <= 30 and mes == 9 or dia >= 1 and dia <= 22 and mes == 10:
    print('Libra')
elif dia >= 23 and dia <= 31 and mes == 10 or dia >= 1 and dia <= 21 and mes == 11:
    print('Escorpião')
elif dia >= 22 and dia <= 30 and mes == 11 or dia >= 1 and dia <= 21 and mes == 12:
    print('Sagitário')
elif dia >= 22 and dia <= 31 and mes == 12 or dia >= 1 and dia <= 19 and mes == 1:
    print('Capricórnio')
elif dia >= 20 and dia <= 31 and mes == 1 or dia >= 1 and dia <= 18 and mes == 2:
    print('Aquário')
elif dia >= 19 and dia <= 28 and mes == 2 or dia >= 1 and dia <= 20 and mes == 3:
    print('Peixes')