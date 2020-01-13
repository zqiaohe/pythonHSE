n = int(input())
hl = set()
all = set()
adl = set()
flag = 0
for i in range(n):
    cl = int(input())
    adl = set()
    for j in range(cl):
        lang = input()
        adl.add(lang)
    if bool(hl) == 0 and flag == 0:
        hl = adl
        flag = 1
    else:
        hl = hl & adl & all
    all = all | adl
print(len(hl))
print("\n".join(hl))
print(len(all))
print("\n".join(all))
