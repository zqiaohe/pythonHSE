n = int(input())
maxr = 0
rep = 0
forep = n
while n != 0:
    if n == forep:
        rep += 1
    else:
        forep = n
        rep = 1
    if rep > maxr:
        maxr = rep
    n = int(input())

print(maxr)
