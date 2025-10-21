import csv

def write():
    f = open("data.csv", "w", newline='')
    x = csv.writer(f)
    while True:
        rollno = input("ENTER ROLL NO: ")
        name = input("ENTER NAME: ")
        marks = input("ENTER MARKS: ")
        data = [rollno, name, marks]
        x.writerow(data)
        print()
        print()
        v = input("WANT TO ENTER MORE [Y/N]: ")
        print()
        print()
        if v.upper() == "N":
            break
    f.close()

def reader():
    f = open("data.csv", "r")
    x = csv.reader(f)
    for row in x:
        print(row)
    f.close()

write()
reader()
import csv

def write():
    f = open("data.csv", "w", newline='')
    x = csv.writer(f)
    while True:
        rollno = input("ENTER ROLL NO: ")
        name = input("ENTER NAME: ")
        marks = input("ENTER MARKS: ")
        data = [rollno, name, marks]
        x.writerow(data)
        print()
        print()
        v = input("WANT TO ENTER MORE [Y/N]: ")
        print()
        print()
        if v.upper() == "N":
            break
    f.close()

def reader():
    f = open("data.csv", "r")
    x = csv.reader(f)
    for row in x:
        print(row)
    f.close()

write()
reader()
