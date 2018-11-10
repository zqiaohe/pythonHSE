a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
if d * e <= a * b:
    if (d <= a and e <= b) or (d <= b and e <= a):
        print('YES')
    else:
        print('NO')
elif d * e <= a * c:
    if (d <= a and e <= c) or (d <= c and e <= a):
        print('YES')
    else:
        print('NO')
elif d * e <= b * c:
    if (d <= c and e <= b) or (d <= b and e <= ac):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
