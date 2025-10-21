# Writing lines to the file
with open("xyz.txt", "w") as f:
    f.write("Johadosi iad sp iads\n")
    f.write("Osdkh kjsda ksd k ds\n")
    f.write("Jods osd ids ods\n")

# Lists to store lines starting with 'J' and 'O'
lis = []
lis2 = []

# Reading lines from the file
with open("xyz.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line[0] == "J":
            lis.append(line)
        elif line[0] == "O":
            lis2.append(line)

# Printing the lines starting with 'J' and 'O'
print("Lines starting with 'J':")
for line in lis:
    print(line, end="")

print("\nLines starting with 'O':")
for line in lis2:
    print(line, end="")
