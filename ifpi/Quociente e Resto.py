#A variável"dividendo" recebe, convertido para inteiro, a leitura do dividendo que é feita pelo teclado.
dividendo=float(input())
#A variável"divisor" recebe, convertido para inteiro, a leitura do divisor que é feita pelo teclado.
divisor=float(input())
#A variável “quociente” recebe o resultado da fórmula de cálculo do quociente da divisão.
quociente=dividendo//divisor
#A variável “resto” recebe o resultado da fórmula de cálculo do resto da divisão.
resto=dividendo%divisor
#Imprime o valor do dividendo, divisor, quociente e resto.
print("{0:.4f}".format(round(quociente,4)))
print("{0:.4f}".format(round(resto,4)))