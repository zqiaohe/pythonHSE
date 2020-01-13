n = int(input())
hl = set()
all = set()
adl = set()
for i in range(n):
    flag = 0
    cl = int(input())
    adl = set()
    for j in range(cl):
        lang = input()
        all.add(lang)
        adl.add(lang)
    #print(hl)
    if bool(hl):
        #print('sss', hl)
        if bool(hl&adl):
            hl = set()
            flag = 1
        else:
            if flag == 0:
                hl= hl&adl
    else:
        #print('asasss', hl)
        hl |= adl
print(len(hl))
print("\n".join(hl))
print(len(all))
print("\n".join(all))
