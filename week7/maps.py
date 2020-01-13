import sys

text = ""
for line in sys.stdin:
    text = text + line
seq = map(str, text.split())
countDict = {}
l = []
for elem in seq:
    countDict[elem] = countDict.get(elem, 0) + 1
    l.append(countDict[elem] - 1)
print(' '.join(map(str, l)))
