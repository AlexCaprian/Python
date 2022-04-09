#Data Atual
da = int(input('Dia Atual:'))
ma = int(input('Mês Atual:'))
aa = int(input('Ano Atual:'))
#Data de Nascimento
dn = int(input('Dia do seu nascimento:'))
mn = int(input('Mês do seu nascimento:'))
an = int(input('Ano do seu nascimento:'))

i = aa - an

if ma < mn:
    i -= 1
elif ma == mn:
    if da < dn:
        i -= 1

print(f'Você tem exatamente {i} anos.')