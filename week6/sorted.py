inp = list(map(int, input().split()))
p = inp[0]
n = inp[1]
arc = []
while n > 0:
    arc.append(int(input()))
    n -= 1
arc = sorted(arc)
n = 0
i = 0
while p - n > 0:
    # print(n)
    n = n + arc[i]
    i += 1
print(i - 1)
