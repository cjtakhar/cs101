import mysql.connector as sq

mydb=sq.connect(host="localhost",user="cs101",passwd="dataisfun",buffered=True)

mycursor=mydb.cursor()

mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)

mycursor.execute("select * from cookies.sales")

result = mycursor.fetchall()

for row in result:
    print(row)

mydb.close()
