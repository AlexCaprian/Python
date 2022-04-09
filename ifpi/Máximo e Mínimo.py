n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

def maximo(n1, n2, n3, n4, n5):
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        return print(n1)
    elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
        return print(n2)
    elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
        return print(n3)
    elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
        return print(n4)
    elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
        return print(n5)

def minimo(n1, n2, n3, n4, n5):
    if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
        return print(n1)
    elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
        return print(n2)
    elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
        return print(n3)
    elif n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
        return print(n4)
    elif n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4:
        return print(n5)

maximo(n1, n2, n3, n4, n5)
minimo(n1, n2, n3, n4, n5)