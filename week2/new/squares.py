import math

n = int(input())
maximumn = math.sqrt(n)
n = 1
while n <= maximumn:
    print(n * n)
    n = n + 1
