numList = list(map(int, input().split()))
minn, maxx, imin, imax = numList[0], numList[0], 0, 0
for i, num in enumerate(numList, start=0):
    if num < minn:
        imin = i
        minn = num
    if num > maxx:
        imax = i
        maxx = num
temp = numList[imin]
numList[imin] = numList[imax]
numList[imax] = temp
print(' '.join(map(str, numList)))
