def sum(a, b):
    if b == 0:
        return a
    elif b == 1:
        return a + 1
    else:
        b = b - 1
        a = a + 1
        return sum(a, b)


a = int(input())
b = int(input())
print(sum(a, b))
