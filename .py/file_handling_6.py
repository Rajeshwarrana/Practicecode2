import pickle 
li=[]
def write():
    f=open("stud.dat","ab")
    while True:
        _name_=input("ENTER YOUR NAME := ")
        _rno_=input("ENTER ROLL NO := ")
        _class_=input("ENTER YOUR CLASS := ")
        _li_=[_rno_,_name_,_class_]
        li.append(_li_)
        print()
        print()
        v=input("WANT TO ADD MORE :- Y/N  :- ")
        print()
        print()
        if v=="N":
            break 
        else:
            pass
        pickle.dump(li,f)

    f.close()

def read():
    f=open("stud.dat","rb")
    x=pickle.load(f)
    y=pickle.load(f)
    z=pickle.load(f)
    print(x)
    print(z)
    print(y)
    f.close()


write()
read()



