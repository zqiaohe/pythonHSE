import math as m

a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
print(m.sqrt(p * (p - a) * (p - b) * (p - c)))
