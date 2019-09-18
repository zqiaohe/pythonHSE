numList = list(map(int, input().split()))
ll = []
last = numList[0]
for i, item in enumerate(numList):
    if item > last:
        ll.append(item)
    last = item
print(' '.join(map(str, ll)))
