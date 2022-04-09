soma = 0
cont = 0
for c in range(0, 501):
    if c % 2 == 0:
        cont += 1
        soma += c
print(f'A soma de {cont} é {soma}')