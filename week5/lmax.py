numList = list(map(int, input().split()))
lmax = 0
idx = 0
for i, item in enumerate(numList):
    if item >= lmax:
        lmax = item
        idx = i
print(lmax, idx)
