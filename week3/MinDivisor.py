def MinDivisor(x):
    if x % 2 == 0:
        return 2
    for i in range(2, x + 1):
        if i > (x ** 0.5):
            return x
        if x % i == 0:
            return i


x = int(input())
print(MinDivisor(x))
