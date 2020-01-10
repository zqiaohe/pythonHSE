inf = int(input())
strn = ''
yes = set(range(1, inf + 1))
no = set()
inp = set()
f = 0
while strn != "HELP":
    strn = input()
    if strn == "YES":
        yes &= inp
    elif strn == "NO":
        yes -= inp
    elif strn != "HELP":
        inp = set(map(int, strn.split()))
print(' '.join(map(str, sorted(yes))))
