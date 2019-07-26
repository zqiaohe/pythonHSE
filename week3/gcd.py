def gcd(a, b):
    minn = min(a, b)
    maxx = max(a, b)
    if maxx % minn == 0:
        return minn
    else:
        return gcd(minn, maxx % minn)


a = int(input())
b = int(input())
nod = gcd(a, b)
print(int(a / nod), int(b / nod))
