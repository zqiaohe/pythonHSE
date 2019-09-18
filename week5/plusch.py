numList = list(map(int, input().split()))
lmax = 0;
max = 0;
for i in numList:
    if i > max:
        lmax = max
        max = i
print(max, lmax)
