import pickle 

def CreateFile():
    f = open("BOOK.dat", "wb")
    pickle.dump(["BOOKNO", "BOOK_NAME", "AUTHOR", "PRICE"], f)
    while True:
        bno = input("ENTER BOOK NO: ")
        bname = input("ENTER BOOK NAME: ")
        bauth = input("ENTER AUTHOR OF BOOK: ")
        bprice = input("ENTER PRICE OF BOOK: ")
        data = [bno, bname, bauth, bprice]
        pickle.dump(data, f)
        v = input("WANT TO ADD MORE DATA [Y/N]: ")
        if v.upper() == "N":
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

CreateFile()
search_name = input("ENTER NAME TO SEARCH: ")
countrec(search_name)

