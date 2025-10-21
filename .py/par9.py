"""Write a method/function DISPLAYWORDS() in python to read lines from a text
 file STORY.TXT, and display those words, which are less than 4 characters.
CBSE Sample Paper (2019-20)"""


def DISPLAYWORDS():
    f=open("xyz.txt","r")
    x=f.read()
    lis=[]
    sl=x.split()
    for i in sl:
        if len(i)<4:
            lis.append(i)
        else:
            pass
    print(lis)
    print(len(lis))
    f.close()


DISPLAYWORDS()
