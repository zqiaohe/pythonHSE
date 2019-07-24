a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a != 0 and b != 0 and c != 0 and d != 0:
    y = (f * a - c * e) / (a * d - c * b)
    x = (e - b * y) / a
elif a == 0:
    y = e / b
    x = (f - d * y) / c
elif b == 0:
    x = e / a
    y = (f - c * x) / d
print(x, y)
