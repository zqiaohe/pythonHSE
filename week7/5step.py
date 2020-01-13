from functools import reduce


def step(a,b):
    a, b = (a**5) * b
    return a

print(reduce(step, map(int, input().split())))
