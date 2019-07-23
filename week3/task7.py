import math

a = float(input())
b = float(input())
c = float(input())
d = b * b - 4 * a * c
if d > 0:
    d = math.sqrt(d)
    minx = min((-b - d) / (2 * a), (-b + d) / (2 * a))
    maxx = max((-b - d) / (2 * a), (-b + d) / (2 * a))
    print(minx, maxx)
elif d == 0:
    print(-b / (2 * a))
else:
    1 + 1
