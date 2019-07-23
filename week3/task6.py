import math

p = int(input())
x = int(input())
y = int(input())
xp = x * p
yp = y * p
x = x + xp / 100
y = y + yp / 100 + xp % 100
x = x + int(y / 100)
y = y % 100
print(int(x), int(y))
