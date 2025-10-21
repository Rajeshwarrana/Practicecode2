'''Ranjan Kumar of class 12 is writing a program to create a CSV |
file “user.csv” which will contain user name and password for
some entries. He has written the following code. As a |
programmer, help him to successfully execute the given task.'''

import csv
f=open("user.csv","w")
x=csv.writer(f)
x.writerow(["USERID","PASSWD"])
while True:
    ud=input("ENTER ID :- ")
    pas=input("ENTER PASSWORD :- ")
    data=[ud,pas]
    v=input("WANT TO ENTER MORE [Y/N] :- ")
    if v.upper()=="N":
        break 
x.writerows(data)
f.close()
