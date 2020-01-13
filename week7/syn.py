n = int(input())
syns1 = {}
syns2 = {}
for i in range(n):
    pair = input().split()
    syns1[pair[0]] = pair[1]
    syns2[pair[1]] = pair[0]
k = input()
if syns1.get(k, '') == '':
    print(syns2.get(k, ''))
else:
    print(syns1.get(k, ''))
