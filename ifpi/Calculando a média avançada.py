def media(a, b, c):
    m=(a+b+c)/3
    return m


n1 = int(input())
n2 = int(input())
n3 = int(input())
m = media(n1, n2, n3)


if n3 > 8:
    m = m+1

if m >= 10:
    m = 10

print(f'{m:.2f}')