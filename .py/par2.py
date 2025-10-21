f=open("example.txt","w")
f.write("juiqgfeorlflhr8 pw qur9q u")
f.write("ouiqgfeorlflhr8 pw qur9q u")
f.write("juiqgfeorlflhr8 pw qur9q u")
f.write("ouiqgfeorlflhr8 pw qur9q u")
f.write("juiqgfeorlflhr8 pw qur9q u")
f.write("juiqgfeorlflhr8 pw qur9q u")
f.write("ouiqgfeorlflhr8 pw qur9q u")
f.close()

f = open("example.txt", "r")
lis = []
lis2 = []

x = f.readlines()
for i in x:
    if i[0].upper() == "J":
        lis.append(i)
    elif i[0].upper() == "O":
        lis2.append(i)
    else:
        pass

# Close the file after reading
f.close()

# Printing the results
print("Lines starting with 'J':", lis)
print("Lines starting with 'O':", lis2)

