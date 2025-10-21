import pickle
f=open("detail.dat","wb")
_student_=int(input("ENTER NUMBER OF STUDENT :- "))
for x in range(_student_):
    _name_=input("ENTER YOUR NAME :- ")
    _rollno_=input("ENTER YOUR ROLLNO :- ")
    lis=[_name_,_rollno_]
    pickle.dump(lis,f)
f.close()

f=open("detail.dat","rb")
_name_=input("ENTER YOUR ROLL NO TO FIND  :- ")
while True:
    pickle.load(f)
    if lis[1]==_name_:
        print(lis[1])
        


    







    
    






       

