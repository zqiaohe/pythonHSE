n = int(input())
k = 0
for i in range(1, n + 1):
    s = ''.join(str(tuple(range(1, i + 1))).split(','))[1:-1].split(' ')
    print(''.join(s))
