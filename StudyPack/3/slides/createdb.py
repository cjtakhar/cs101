from dotenv import load_dotenv
import os
import mysql.connector as sq

load_dotenv()

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

# Connect to MySQL Server
mydb = sq.connect(host="localhost", user=db_user, passwd=db_password)
mycursor = mydb.cursor()

# Create Database (if not exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS qctestdb")

# Connect to the newly created database
mydb = sq.connect(host="localhost", user="kt", passwd="takhar35", database="qctestdb")
mycursor = mydb.cursor()

# Create Table (if not exists)
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS testresults (
        plant INT NOT NULL, 
        testresults TEXT NOT NULL, 
        zipcode INT NOT NULL, 
        PRIMARY KEY (plant)
    )
""")

# Corrected Values List
values = [
    (1001, "B1234PABQ50D20230908", 93722), 
    (1002, "B1234PABQ0050D20230908B5678PXYQ0030D20230909", 1960), 
    (1006, "B1234PABQ50D20230908", 93722), 
    (1007, "B2021PGEQ25D20230103", 77433), 
    (1008, "B4521PABQ56D20230315", 33023)
]

# SQL Insert Command
SQLCMD = "INSERT INTO testresults (plant, testresults, zipcode) VALUES (%s, %s, %s)"

# Execute Insert Statement
mycursor.executemany(SQLCMD, values)

# Commit changes and close connection
mydb.commit()
mycursor.close()
mydb.close()

print("Database and table created successfully, and data inserted.")
