import mysql.connector as m 
mydb=m.connect(host='loalhost',user='root',passwd='root',database='class12')
if mydb.is_connected()==True:
    print("CONNECTED SUCCESSFULLY !!")

