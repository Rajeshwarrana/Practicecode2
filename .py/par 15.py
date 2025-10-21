import csv
def ADD():
    f=open("dt.csv","w")
    x=csv.writer(f)
    x.writerow(["EMPID","NAME","MOBILE"])
    while True:
        emp=input("ENTER EMP ID :-  ")
        name=input("ENTER NAME :-  ")
        mobile=input("ENTER MOBILE :-  ")
        data=[emp,name,mobile]
        v=input("WANT TO ADD MORE DATA :-  ")
        if v.upper()=="N":
            break 
    x.writerows(data) 
    f.close()


def count():
    f=open("dt.csv","r")
    x=csv.reader(f)
    next(x)
    count=0
    for i in x:
        count+=1 
    print(count)

ADD()
count()

        
        