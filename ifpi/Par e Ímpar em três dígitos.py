def par(a):
    return a%2 == 0

n = int(input())

u = n//1%10
d = n//10%10
c = n//100%10

uv = par(u)
dv = par(d)
cv = par(c)

if n >= 1000 or n <= 99:
    None
elif (uv, dv, cv) == (False, True, True) or (uv, dv, cv) == (True, False, True) or (uv, dv, cv) == (True, True, False):
    print('2')
elif (uv, dv, cv) == (False, True, False) or (uv, dv, cv) == (False, False, True) or (uv, dv, cv) == (True, False, False):
    print('1')
elif (uv, dv, cv) == (False, False, False):
    print('0')
else:
    print('3')