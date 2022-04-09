#A variável “n” recebe, convertido para inteira, a leitura do valor de 100 a 999 que é feita pelo teclado.
n=int(input('Digite um número entre 100 e 999:'))
#A variável “u” recebe o resultado da fórmula de cálculo da unidade.
u=n%10
#A variável “n” recebe o resultado da fórmula de cálculo do número.
n=n//10
#A variável “d” recebe o resultado da fórmula de cálculo de dezena.
d=n%10
#A variável “n” recebe o resultado da fórmula de cálculo do número.
n=n//10
#A variável “c” recebe o resultado da fórmula de cálculo de centena.
c=n%10
#Imprime na tela a unidade, dezena e centena.
print(f'Unidade: {u}, dezena: {d}, centena {c}')