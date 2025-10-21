#WRITE A METHOD IN PYTHON ONLY THOSE WORD WHOSE LENGTH IS 5
lis=[]
f=open("xyz.txt","r")
x=f.read()
for i in x:
    if i[0]=="O":
        lis.append(i)
print(lis)
print(x)
