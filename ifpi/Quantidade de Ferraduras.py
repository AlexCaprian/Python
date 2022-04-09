#A variável “qc” recebe, convertido para inteira, a leitura da quantidade de cavalos que é feita pelo teclado.
qc=int(input('Quantidade de cavalos no haras:'))
#A variável “f” recebe o resultado da fórmula de cálculo da quantidade de ferradura.
f=qc*4
#Imprime na tela a quantidade de ferraduras.
print(f'São necessárias {f} ferraduras para o haras.')