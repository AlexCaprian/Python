#A variável 'n' recebe um valor pelo teclado do usuário.
n=int(input('Em que ano você nasceu?'))
##A variável 'a' recebe um valor pelo teclado do usuário.
a=int(input('Para qual ano você quer saber sua idade?'))
#A variável 'c' recebe um valor do resultado da formula de calculo entre a e n
c=a-n
#imprime 'Se você nasceu em {n} em {a} você terá {c}'
print(f'Se você nasceu em {n} em {a} você terá {c}')