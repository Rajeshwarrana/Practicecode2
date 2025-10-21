"""Write a function Show_words() in python to read the content of
a text file 'NOTES.TXT' and display the entire content in capital letters. 
Example, if the file contains: "This is a test file"
Then the function should display the output as: THIS IS A TEST FILE
S"""



def Show_words():
    f=open("xyz.txt","r")
    x=f.read()
    print("OLD ONE :- ")
    print()
    print(x)
    print()
    print("IN UPPER CASE :- ")
    data=x.upper()
    print()
    print(data)
    print()
    print()
    

Show_words()
