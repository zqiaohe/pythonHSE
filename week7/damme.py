import sys

text = ""
for line in sys.stdin:
    text = text + line
seq = map(str, text.split())
countDict = {}
freqword = ()
freqlist = []
for elem in seq:
    countDict[elem] = countDict.get(elem, 0) + 1
for elem in countDict:
    freqword = (countDict[elem], elem)
    freqlist.append(freqword)
for i in sorted(freqlist, key=lambda x: (-x[0], x[1])):
    print(i[1])
