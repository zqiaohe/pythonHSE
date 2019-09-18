numList = list(map(int, input().split()))
chet = ' '.join([str(x) for x in numList if x % 2 == 0])
print(chet)
