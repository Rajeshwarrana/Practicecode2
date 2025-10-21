f=open(r"C:\Users\Rajeshwar rana\Desktop\CS PRACTICALS\ttt.txt",'r')
p=f.read()
x=p.split()
for v in x:
    print(v,end="#")
print()
f.close()

