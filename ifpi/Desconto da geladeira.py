#A variável “v” recebe, convertido para real, a leitura do valor da geladeira que é feita pelo teclado.
v=float(input('Valor da geladeira:'))
#A variável “d” recebe, convertido para real, a leitura do percentual do desconto que é feita pelo teclado.
d=float(input('Percentual do desconto:'))
#A variável “f” recebe o resultado da fórmula de cálculo do fator.
f=1-d/100
#A variável “v2” recebe o resultado da fórmula de cálculo do valor com desconto.
v2=v*f
#Imprime na tela o valor do percentual do desconto e do valor com desconto.
print(f'A geladeira com {d}% de desconto fica por {v2:.2f}')