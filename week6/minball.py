class Student:
    F = ""
    I = ""
    Ball1 = 0
    Ball2 = 0
    Ball3 = 0

    def Print(self):
        print(self.F, self.I, self.Ball1, self.Ball2, self.Ball3)


inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
slist = []
m = int(lines[0])
for line in lines:
    line = line.replace("\uFEFF", "")
    line = line.replace("\n", "")
    k = line.split(' ')
    if len(k) < 2:
        continue
    student = Student()
    student.Ball1 = int(k[len(k) - 1])
    student.Ball2 = int(k[len(k) - 2])
    student.Ball3 = int(k[len(k) - 3])
    slist.append(student)
slist.sort(key=lambda x: x.Ball1 + x.Ball2 + x.Ball3)
ball = slist[m - 1].Ball1 + slist[m - 1].Ball2 + slist[m - 1].Ball3
inFile.close()
print(ball, file=outFile)
