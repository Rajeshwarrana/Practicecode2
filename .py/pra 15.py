import csv
def add():
    f=open("furdata.csv","w")
    x=csv.writer(f)
    x.writerow(["FID","FNAME","FPRICE"])
    while True:
        fid=input("ENTER ID :- ")
        fname=input("ENTER NAME :- ")
        fprice=input("ENTER PRICE :- ")
        data=[fid,fname,fprice]
        v=input("WANT TO ENTER MORE DATA [Y/N] :- ")
        if v.upper()=="N":
            break
    x.writerows(data)
    f.close()



def search():
    with open("furdata.csv", "r") as f:
        x = csv.reader(f)
        next(x)  # Skip the header row
        for i in x:
            if len(i) >= 3:  # Check if the row has at least 3 elements
                if int(i[2]) > 1000:
                    print(i)
            else:
                print("Invalid row:", i)


add()
search()
