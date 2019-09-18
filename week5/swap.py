numList = list(map(int, input().split()))
i1 = 0;
i2 = 0;
minn = numList[0]
maxx = numList[0]
for i, num in enumerate(numList, start=0):
    if num < minn:

print(' '.join(map(str, numList)))
