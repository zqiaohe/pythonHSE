n = int(input())
str1 = '+___ ' * n
str2 = '|1 / '
str3 = '|__\ ' * n
str4 = '|    ' * n

for i in range(2, n + 1):
    f = '|' + str(i) + ' / '
    str2 = str2 + f
print(str1)
print(str2)
print(str3)
print(str4)
