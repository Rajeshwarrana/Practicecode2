import pickle 
data=[]
def write():
    f=open("dex.dat","wb")
    while True:
        rollno=input("ENTER ROLL NO :- ")
        name=input("ENTER NAME :- ")
        marks=input("ENTER MARKS :- ")
        lis=[rollno,name,marks]
        data.append(lis)
        print()
        print()
        pickle.dump(data,f)
        v=input("CHOOSE AND CONTINUE :- \nY\nN         :- ")
        print()
        print()
        if v=="N":
            break 
        else:
            pass
    f.close()  

def read():
    f=open("dex.dat","rb")
    x=pickle.load(f)
    for i in x:
        print(i)
    f.close()


write()
read()
