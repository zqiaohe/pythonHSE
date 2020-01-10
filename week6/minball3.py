inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.read().splitlines()
slist = []
n = int(lines[0])
del lines[0]
for line in lines:
    line = line.replace("\uFEFF", "")
    line = line.replace("\n", "")
    k = line.split(' ')
    if (int(k[-3]) >= 40 and int(k[-2]) >= 40 and int(k[-1]) >= 40):
        slist.append(int(k[-3]) + int(k[-2]) + int(k[-1]))

slist.sort(reverse=True)
if len(slist) <= n:
    print(0, file=outFile)
elif slist[n] == slist[0]:
    print(1, file=outFile)
elif slist[n] == slist[n - 1]:
    j = 1
    while slist[n - j + 1] == slist[n - j]:
        j += 1
    print(slist[n - j], file=outFile)
else:
    print(slist[n - 1], file=outFile)
inFile.close()
outFile.close()
