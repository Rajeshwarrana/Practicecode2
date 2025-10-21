"""Write the definition of a function Count_Line() in Python,# which should 
read each line of a text file "SHIVAJI.TXT" and count 
total number of lines present in text file."""


f=open("xyz.txt","r")
x=f.readlines()
y=len(x)
print(y)
