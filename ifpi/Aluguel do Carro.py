#A variável “d” recebe, convertido para inteiro, a leitura da quantidade de dias que é feita pelo teclado.
d=int(input('Quantidade de dias alugados:'))
#A variável “km” recebe, convertido para real, a leitura do km percorridos que é feita pelo teclado.
km=float(input('Quantos Km foram percorridos:'))
#A variável “t” recebe o resultado da fórmula de cálculo do aluguel.
t=(d*60)+(km*0.15)
#Imprime na tela o valor do aluguel.
print(f'O total a pagar pelo alugel é de R$ {t:.2f}')