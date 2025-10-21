import pickle 
data=[]
def write_data():
    f=open("dex.dat","wb")
    while True:
        rollno=input("ENTER ROLL NO :- ")
        name=input("ENTER NAME :- ")
        marks=input("ENTER MARKS :- ")
        lis=[rollno,name,marks]
        data.append(lis)
        print()
        print()
        v=input("CHOOSE AND CONTINUE? [Y/N] :- ")
        print()
        print()
        if v=="N":
            break 
        else:
            pass
    pickle.dump(data,f)
    f.close()  

def read_data():
    f=open("dex.dat","rb")
    x=pickle.load(f)
    for i in x:
        print(i)

def search_data():
    f=open("dex.dat","rb")
    x=pickle.load(f)
    src_itm=input("ENTER ROLLNO TO SEARCH :- ")
    for i in x :
        if i[0]==src_itm:
            print(i)

def max_binary():
    f=open("dex.dat","rb")
    x=pickle.load(f)
    for i in x :
        if i[2]ismax()




write_data()
read_data()
search_data()

