x = []
now = int(input())
while now != 0:
    x.append(now)
    now = int(input())
x.sort(reverse=True)
print(x[1])
