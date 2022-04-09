#A variável"minutes" recebe, convertido para inteiro, a leitura do minuto que é feita pelo teclado.
m=int(input())
#A variável “h” recebe o resultado da fórmula de cálculo dos minutos convertido em horas.
h=m//60
#A variável “m” recebe o resultado da fórmula de cálculo do resto dos minutos convertido em horas.
min=m%60
#Imprime o valor dos minutos e dos minutos convertidos em horas.
print(f'{h}h{min}min')