inf = int(input())
yes = set()
no = set()
inp = set()
strn = ''
while strn != "HELP":
    strn = input()
    if strn == "YES":
        yes = yes & yes
    elif strn == "NO":
        no = (no | inp)
    elif strn != "HELP":
        inp = set(map(int, strn.split()))
print(' '.join(map(str, yes - no)))
