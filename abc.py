a = int(input())
b = int(input())
c = int(input())
aa = a >= b and a >= c
bb = b >= a and b >= c
cc = c >= a and c >= b
if aa:
    print(a)
elif bb:
    print(b)
elif cc:
    print(c)
