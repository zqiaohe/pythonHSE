numList = list(map(int, input().split()))
for i in numList:
    if i > 0:
        minim = i
        for j in numList:
            if j < minim and j > 0:
                minim = j
        break
print(minim)
