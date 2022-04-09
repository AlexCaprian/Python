#A variável “lme” recebe, convertido para real, a leitura do valor do lado menor do terreno que é feita pelo teclado.
lme=float(input('Lado menor do terreno:'))
#A variável “lma” recebe, convertido para real, a leitura do valor do lado maior do terreno que é feita pelo teclado.
lma=float(input('Lado aior do terreno:'))
#A variável “a” recebe o resultado da fórmula de cálculo da área do terreno.
a=lme*lma
#A variável “p” recebe o resultado da fórmula de cálculo do perímetro do terreno.
p=(2*lme)+(2*lma)
#Imprime na tela o valor da área do terreno.
print(f'Área do Terreno: {a}')
#Imprime na tela o valor do perímetro do terreno.
print(f'Perímento do Terreno: {p}')