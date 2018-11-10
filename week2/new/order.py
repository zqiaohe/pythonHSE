a, b, c = int(input()), int(input()), int(input())
if a >= b:
    a, b = b, a
if c <= a:
    a, b, c = c, a, b
elif c <= b:
    a, b, c = a, c, b
print(a, b, c)
