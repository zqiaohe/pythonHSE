n = int(input())
sels = list(map(int, input().split()))
m = int(input())
bombs = list(map(int, input().split()))
s = []
b = []


def sr(mau):
    return mau[1]


for index, i in enumerate(sels):
    x = (index + 1, i)
    s.append(x)

for index, i in enumerate(bombs):
    x = (index + 1, i)
    b.append(x)
s.sort(key=sr)
b.sort(key=sr)
k = 0
i = 0
j = 0
minn = abs(s[0][1] - b[0][1])
lastdest = abs(s[0][1] - b[0][1])
while i < len(s):
    j = k
    minn = abs(s[i][1] - b[j][1]) + 1
    sels[s[i][0] - 1] = b[j][0]
    while j < len(b):
        if abs(s[i][1] - b[j][1]) < minn:
            minn = abs(s[i][1] - b[j][1])
            k = j
            sels[s[i][0] - 1] = b[j][0]
        if abs(s[i][1] - b[j][1]) > minn:
            break
        #print(s[i], b[j], minn)
        j += 1
    i += 1
# print(ss)
print(' '.join(map(str, sels)))
