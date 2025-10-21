"""A binary file "PLANTS.dat" has structure (ID, NAME, PRICE). 
• Write the definition of a function WRITEREC() in Python, to input data
for records from the user and write them to the file PLANTS.dat. 
• Write the definition of a function SHOWHIGH() in Python, which 
reads the records of PLANTS.dat and displays those records for 
which the PRICE is more than 500."""



import pickle

def WRITEREC():
    f=open("PLANT.dat","wb")
    data=[]
    while True:
        id=input("ENTER ID :-  ")
        name=input("ENTER NAME :-  ")
        price=input("ENTER PRICE :-  ")
        lis=[id,name,price]
        data.append(lis)
        print()
        print()
        v=input("WANT TO ENTER MORE [Y/N] :-  ")
        print()
        print()
        if v.upper()=="N":
            break
    pickle.dump(data,f)
    f.close()


def SHOWHIGH():
    f=open("PLANT.dat","rb")
    x=pickle.load(f)
    data=[]
    for i in x:
        if int(i[2])>500:
            data.append(i)
        else:
            pass

    print()
    print()
    print(data)
    f.close()


WRITEREC()
SHOWHIGH()



        

    