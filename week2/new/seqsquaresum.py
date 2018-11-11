now = 1
n = int(input())
seqSum = 0
while now <= n:
    seqSum += now * now
    now += 1
print(seqSum)