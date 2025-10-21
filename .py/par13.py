f=open("xyz.txt","r")
x=f.readlines()
lis=[]
for i in x:
    if i[0] in ['a','e','i','o','u','A','E','I','O','U']:
        lis.append(i)
        print("✓")

print(lis)



