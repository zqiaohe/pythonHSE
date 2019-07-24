import sys

s = input()
a = s.find('f')
if a == -1:
    print(-2)
    sys.exit(0)
b = s[a + 1:]
c = b.find('f')
if c == -1:
    print(-1)
    sys.exit(0)
else:
    print(c + a + 1)
