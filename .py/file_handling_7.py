f=open(r"C:\Users\Rajeshwar rana\Desktop\CS PRACTICALS\ttt.txt",'w')
for i in range(5):
    e=input("ENTER THE DATA YOU WANT TO STORE :- ")
    f.writelines(e)
    f.write("\n")
    
f.close()


f=open(r"C:\Users\Rajeshwar rana\Desktop\CS PRACTICALS\ttt.txt",'r')
x=f.readlines()
print(x)

   
