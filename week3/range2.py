a = int(input())
b = int(input())
if a < b:
    str = str(tuple(range(a, b + 1)))
    str = ' '.join(str.split(','))
    print(str[1:-1])

elif a > b:
    str = str(tuple(range(a, b - 1, -1)))
    str = ' '.join(str.split(','))
    print(str[1:-1])
else:
    print(a)
