"""Aman is a Python programmer. He has written a code and created a binary
file record.dat with employeeid, ename and salary. The file contains 10
records. He now has to update a record based on the employee id entered
by the user and update the salary. The updated record is then to be
written in the file temp.dat. The records which are not to be updated also
have to be written to the file temp.dat. If the employee id is not found, an
appropriate message should to be displayed. As a Python expert, help him
to complete the following code based on the requirement given above:"""



import pickle

# Open the original file for reading in binary mode ('rb')
with open("record.dat", "rb") as f:
    x = pickle.load(f)  # Load the data from the file

up = input("ENTER EID TO UPDATE: ")
sal = input("ENTER SALARY TO BE CHANGED: ")

data = []  # Create an empty list to store updated data
for i in x:
    if i[0] == up:
        # If the EID matches, create a new tuple with the updated salary
        updated_entry = (i[0], i[1], sal)
        data.append(updated_entry)  # Append the updated tuple to the data list
    else:
        data.append(i)  # If the EID doesn't match, keep the original tuple

# Open a temporary file for writing in binary mode ('wb')
with open("temp.dat", "wb") as z:
    pickle.dump(data, z)  # Dump the updated data to the temporary file

    


    