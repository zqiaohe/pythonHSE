a = [int(input()), int(input()), int(input())]
b = [int(input()), int(input()), int(input())]
a.sort()
b.sort()
if (a[0] >= b[0]) and (a[1] >= b[1]) and (a[2] >= b[2]):
    if (a[0] == b[0]) and (a[1] == b[1]) and (a[2] == b[2]):
        print("Boxes are equal")
    else:
        print("The first box is larger than the second one")
else:
    if (a[0] <= b[0]) and (a[1] <= b[1]) and (a[2] <= b[2]):
        print("The first box is smaller than the second one")
    else:
        print("Boxes are incomparable")
