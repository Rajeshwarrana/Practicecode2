def detail():
    import pickle
    _name=input('ENTER YOUR NAME :-  ')
    _rollno=input('ENTER YOUR ROLL NO. :-  ')
    _marks=input('ENTER YOUR MARKS(PHY , CHEM , MATHS , COMP , ENG ) :-  ')
    f=open("school.dat",'ab')
    l=[_name,_rollno,_marks]
    pickle.dump(l,f)
    f.close()

x=int(input("ENTER HOE MANY STUDENTS ARE THEIR  :-  "))
for v in range(x):
    detail()

f=open("school.dat",'rb')
c=f.read()
print(c)



