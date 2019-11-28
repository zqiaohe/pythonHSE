class Student:
    Fam = ""
    Ball = 0


n = int(input())
slist = []
for line in range(n):
    k = input().split(' ')
    student = Student()
    student.Fam = k[0]
    student.Ball = int(k[1])
    slist.append(student)
slist.sort(key=lambda x: x.Ball)

for i in slist:
    print(i.Fam)
