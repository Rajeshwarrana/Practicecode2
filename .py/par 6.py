f=open("xyz.txt","r")
x=f.read()
lis=[]
for i in x:
    if i.isdigit():
        lis.append(i)
    else:
        pass
f.close()
print(lis)
print()
print()
print("TOTAL NO OF DIGIT ",len(lis))

