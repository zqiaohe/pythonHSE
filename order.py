a = int(input())
b = int(input())
c = int(input())
if (a <= b <= c):
    print(a, b, c)
if (b > a):
    (a, b) = (b, a)
elif (c > a):
    (a, c) = (c, a)
