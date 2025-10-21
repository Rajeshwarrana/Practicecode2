import pickle
f=open("detail.dat","wb")
st=input("ENTER NO OF STUDENTS :- ")
lis=["rollno","name","marks"]
for x in st:
    name=input("ENTER YOUR NAME :- ")
    rollno=input("ENTER YOUR ROLLNO :- ")
    marks=input("ENTER YOUR MARKS :- ")
    pickle.dump(name,f)
    pickle.dump(rollno,f)
    pickle.dump(marks,f)
f.close()

f=open("detail.dat","rb")
x=pickle.load(f)
y=pickle.load(f)
z=pickle.load(f)
print(x)
print(y)
print(z)

