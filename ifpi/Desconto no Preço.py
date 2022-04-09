#A variável “preco” recebe, convertido para real, a leitura do preço que é feita pelo teclado.
preco=float(input())
#A variável “preco_com_desconto” recebe o resultado da fórmula de cálculo do desconto.
preco_com_desconto=preco*0.90
#A variável “preco_com_desconto” recebe o arredodamento do resultado da fórmula de cálculo do desconto.
preco_com_desconto=round(preco_com_desconto,2)
#Imprime na tela o valor do desconto.
print(preco_com_desconto)