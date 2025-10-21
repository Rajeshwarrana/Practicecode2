"""Write a function in python to count the number of 
lines in a text file 'STORY.TXT' which is starting with an alphabet 'A'."""




def no_of_line():
    f=open("xyz.txt","r")
    x=f.readlines()
    lis=[]
    for i in x:
        if i[0][0]=="a":
            lis.append(i)
        elif i[0][0]=="A":
            lis.append(i)
        else:
            pass
    print(lis)
 
    f.close()


no_of_line()