class Student:
    Fam = ""
    Name = ""
    Ball = 0


inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
slist = []
for line in lines:
    line = line.replace("\uFEFF", "")
    line = line.replace("\n", "")
    k = line.split(' ')
    student = Student()
    student.Fam = k[0]
    student.Name = k[1]
    student.Ball = k[3]
    slist.append(student)
slist.sort(key=lambda x: x.Fam)
inFile.close()
for i in slist:
    print(i.Fam, i.Name, i.Ball, file=outFile)

outFile.close()
