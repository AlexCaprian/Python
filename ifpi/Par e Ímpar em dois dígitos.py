def impar(a, b):
    if (a, b) == (True, True):
        print('Os dois dígitos são ímpares.')
    elif (a, b) == (False, True) or (a, b) == (True, False):
        print('Apenas um dígito é ímpar.')
    else:
        print('Nenhum dígito é ímpar.')


n = int(input())

u = n//1%10
d = n//10%10

ui = u%2 == 1
di = d%2 == 1

if n < 10:
    None
elif n >= 100:
    None
else:
    impar(ui, di)