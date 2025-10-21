"""A binary file "PATIENTS.dat" has structure (PID, NAME, DISEASE). 
Write the definition of a function countrec() in Python that would read 
contents of the file "PATIENTS.dat" and display the details of those patients 
who have the DISEASE as 'COVID-19'. The function should also display the total 
number of such patients whose DISEASE is 'COVID-19'."""






import csv
def countrec():
    f=open("PATIENTS.csv","w")
    x=csv.writer(f)
    x.writerow(["PID","NAME","DISEASE"])
    while True:
        pid=input("ENTER PID :- ")
        name=input("ENTR NAME :- ")
        dis=input("ENTER DISEASE :- ")
        data=[pid,name,dis]
        v=input("WANT TO ENTER MORE DATA [Y/N] :-  ")
        if v.upper()=="N":
            break 
    x.writerows(data)
    f.close()




def showpt():
    f=open("PATIENTS.csv","r",newline="")
    x=csv.reader(f)
    for i in x:
        print(i)
    f.close()




countrec()
showpt()