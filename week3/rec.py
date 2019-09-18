def rec(a):
    b = int(input())
    if b == 0:
        print(b)
    else:
        rec(b)
    print(a)


a = int(input())
if a != 0:
    rec(a)
else:
    print(a)
