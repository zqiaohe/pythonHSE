def An(a, n):
    if n == 0:
        return 1
    elif n == 2:
        return a * a
    elif n == 1:
        return a
    elif n % 2 == 0:
        return An(a*a, n / 2)
    elif n % 2 != 0:
        return a * An(a, n - 1)


a = float(input())
n = int(input())
print(An(a, n))
