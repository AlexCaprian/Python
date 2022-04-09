#A variável “anos” recebe, convertido para inteiro, a leitura do ano que é feita pelo teclado.
anos=int(input())
#A variável "valor_por_anos" recebe, convertido para real, a leitura do valor por ano que é feita pelo teclado.
valor_por_ano=float(input())
#A variável “bonus” recebe o resultado da fórmula de cálculo do bônus.
bonus=anos*valor_por_ano
#Imprime na tela o valor do bônus.
print("{0:.2f}".format(round(bonus,2)))