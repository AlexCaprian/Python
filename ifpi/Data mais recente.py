import datetime

d1 = int(input())
m1 = int(input())
a1 = int(input())
data1 = (f'{d1}/{m1}/{a1}')

d2 = int(input())
m2 = int(input())
a2 = int(input())
data2 = (f'{d2}/{m2}/{a2}')


data01 = datetime.date(a1, m1, d1)
data02 = datetime.date(a2, m2, d2)

if data01 > data02:
    print(data1)
else:
    print(data2)