def scorecard():
    name=input('enter your name')
    marks=input('enter your marks')
    f=open('marks.txt','a')
    x=f.writelines(name)
    z=f.writelines(marks)
    f.close()


no=int(input('enter no of students in class :- '))
for e in range(no):
    scorecard()


f=open('marks.txt','r')
x=f.readlines()
print(x[0])
print(x[1])
