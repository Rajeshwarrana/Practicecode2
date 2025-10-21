f=open("xyz.txt","r")
x=f.read()
y=x.split()
lis=[]
for i in y:
    if len(i)==5:
        lis.append(i)
    else:
        pass
f.close()
print(lis)

