import sys

text = ""
for line in sys.stdin:
    text = text + line
seq = map(str, text.split())
countDict = {}
words = {}
words2 = {}
l = []
maxval = 0
OrdSet = set()
for elem in seq:
    countDict[elem] = countDict.get(elem, 0) + 1
    if countDict[elem] > maxval:
        maxval = countDict[elem]
for elem in countDict:
    # print(elem, countDict[elem])
    words[countDict[elem]] = words.get(countDict[elem], '') + elem + ' '
for i in range(maxval, 0, -1):
    OrdSet = set(words.get(i, '').split())
    print('\n'.join(sorted(OrdSet)))
