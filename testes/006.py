numero = int(input('Digite um número:'))
total = 0
for primo in range(1, numero + 1):
    if numero % primo == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(primo, end=' ')
print(f'\n\033[mO número {numero} foi divisível {total} vezes.')
if total == 2:
    print('Por isso ele é PRIMO!!!')
else:
    print('Por isso ele não é PRIMO!!!')