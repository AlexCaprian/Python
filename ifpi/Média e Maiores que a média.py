n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

m = (n1+n2+n3+n4+n5)/5
print(f'{m:.2f}')
if n1 > m:
    print(n1)
if n2 > m:
    print(n2)
if n3 > m:
    print(n3)
if n4 > m:
    print(n4)
if n5 > m:
    print(n5)