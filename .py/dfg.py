import pickle

def write_data():
    data = []
    try:
        with open("dex.dat", "wb") as f:
            while True:
                rollno = input("ENTER ROLL NO: ")
                name = input("ENTER NAME: ")
                marks = input("ENTER MARKS: ")
                lis = [rollno, name, marks]
                data.append(lis)
                print()
                print()
                pickle.dump(data, f)
                choice = input("CONTINUE? (Y/N): ").strip().upper()
                print()
                print()
                if choice != 'Y':
                    break
    except Exception as e:
        print("An error occurred:", e)

def read_data():
    try:
        with open("dex.dat", "rb") as f:
            while True:
                try:
                    x = pickle.load(f)
                    for i in x:
                        print(i)
                except EOFError:
                    break
    except FileNotFoundError:
        print("No data found.")

write_data()
read_data()
