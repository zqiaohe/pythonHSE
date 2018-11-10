a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if (d >= a and e >= b) or (d >= b and e >= a):
    print('YES')
elif (d >= a and e >= c) or (d >= c and e >= a):
    print('YES')
elif (d >= c and e >= b) or (d >= b and e >= c):
    print('YES')
else:
    print('NO')
