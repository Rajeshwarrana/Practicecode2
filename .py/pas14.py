f=open("xyz.txt","r")
x=f.read()
count=0
for i in x:
    if i in 'ETet':
        count +=1
    else:
        pass 
print("TOTAL NO OF E AND T ARE : - ",count)
