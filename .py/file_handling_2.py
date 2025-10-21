import csv
f=open("studen.csv","w")
x=csv.writer(f)
x.writerows(["rollno","marks","name"])
for i in range(1):
    name=input("what is your name :- ")
    marks=input("enter your marks :- ")
    rollno=input("enter your rollno :- ")
    rec=[rollno,marks,name]
    x.writerows(rec)
f.close()

f=open("studen.csv","r")
x=csv.reader(f)
for v in x:
    print(x)

