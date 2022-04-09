#A variável"valor_a" recebe, convertido para inteiro, a leitura da variável A que é feita pelo teclado.
valor_a=int(input())
#A variável"valor_b" recebe, convertido para inteiro, a leitura do minuto que é feita pelo teclado.
valor_b=int(input())
#A variável “auxiliar” recebe a variável "valor_a".
auxiliar=valor_a
#A variável “valor_a” recebe a variável "valor_b".
valor_a=valor_b
#A variável “valor_b” recebe a variável "auxiliar".
valor_b=auxiliar
#Imprime o valor da variável A.
print(f'{valor_a}')
#Imprime o valor da variável B.
print(f'{valor_b}')