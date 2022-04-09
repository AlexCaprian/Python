n = str(input('Digite uma frase:').strip().upper())
m = n.split()
j = ''.join(m)
i = ''
for c in range(len(j)-1, -1, -1):
    i += j[c]
print(f'{j} ao contrário é {i}.')

if j == i:
    print('Por isso ele é um POLÍNDROMO.')
else:
    print('Por isso ele não é um POLÍNDROMO.')