x = int(input())
maximum = x
secondmax = x
while x != 0:
    if x > maximum:
        secondmax = maximum
        maximum = x
    x = int(input())
print(secondmax)
