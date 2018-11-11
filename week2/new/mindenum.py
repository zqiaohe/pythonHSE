n = int(input())
i = 2
while i <= n:
    if n % i != 0:
        i = i + 1
    else:
        print(i)
        break
