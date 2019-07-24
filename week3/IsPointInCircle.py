import math


def IsPointInCircle(x, y, xc, yc, r):
    d = (xc - x) * (xc - x) + (yc - y) * (yc - y)
    return (math.sqrt(d) <= r)


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
