my_list = list(map(int, input().split()))
B = set()
for now in my_list:
    g = set()
    g.add(now)
    if g <= B:
        print('YES')
    else:
        B.add(now)
        print('NO')
