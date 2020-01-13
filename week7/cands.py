inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.read().splitlines()
countDict = {}
freqword = ()
freqlist = []
sum = 0
for line in lines:
    line = line.replace("\uFEFF", "")
    line = line.replace("\n", "")
    countDict[line] = countDict.get(line, 0) + 1
    sum += 1
for elem in countDict:
    freqword = (countDict[elem], elem)
    freqlist.append(freqword)

cands = sorted(freqlist, key=lambda x: (-x[0]))
if cands[0][0] > sum / 2:
    print(cands[0][1], file=outFile)
else:
    print(cands[0][1], file=outFile)
    print(cands[1][1], file=outFile)
inFile.close()
outFile.close()
