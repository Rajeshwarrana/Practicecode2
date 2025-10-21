"""A binary file “Book.dat” has structure CBSE Sample Paper (2020-21)
[BookNo, Book_Name, Author, Price].

i. Write a user defined function CreateFile() to input data for a
record and add to Book.dat .

ii. Write a function CountRec(Author) in Python which accepts the
Author name as parameter and count and return number of
books by the given Author are stored in the binary file
“Book.dat”"""



import pickle 

def CreatFile():
    f=open("BOOK.dat","wb")
    pickle.dump(["BOOKNO","BOOK_NAME","AUTHOR","PRICE"],f)
    while True:
        bno=input("ENTER BOOK NO :- ")
        bname=input("ENTER NOOK NAME :- ")
        bauth=input("ENTER AUTHOR OF BOOK :- ")
        bprice=input("ENTER PRICE OF BOOK :- ")
        data=[bno,bname,bauth,bprice]
        pickle.dump(data,f)
        v=input("WANT TO ADD MORE DATA [Y/N] :- ")
        if v.upper()=="N":
            break 
    
    f.close()



def countrec(name_to_search):
    f = open("BOOK.dat", "rb")
    # Skip the first record (header)
    header = pickle.load(f)
    print(header)
    count = 0
    while True:
        try:
            data = pickle.load(f)
            if data[2] == name_to_search:
                print(data)
                count += 1
        except EOFError:
            break
    print(f"Total books found with author '{name_to_search}': {count}")
    f.close()

CreatFile()
search_name = input("ENTER NAME TO SEARCH: ")
countrec(search_name)





