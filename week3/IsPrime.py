def IsPrime(x):
    for i in range(2, x + 1):
        if i > (x ** 0.5):
            return 'YES'
        if x % i == 0:
            return 'NO'


x = int(input())
print(IsPrime(x))
