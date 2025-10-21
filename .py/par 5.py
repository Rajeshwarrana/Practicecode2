f=open("xyz.txt","r")
x=f.readlines()
lis=[]
for i in x:
    if len(i)>20:
        lis.append(i)
    else:
        pass
f.close()
print(lis)
