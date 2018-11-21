x = []
now = int(input())
while now != 0:
    x.append(now)
    now = int(input())
x.sort(reverse=True)
max = x[0]
num = 0
for i in x:
    if i == max:
        num += 1
    else:
        break
print(num)
