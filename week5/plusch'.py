numList = list(map(int, input().split()))
chet = [str(x) for x in numList if x > 0]
print(len(chet))
