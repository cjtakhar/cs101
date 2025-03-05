#import libraries
import mysql.connector as sq

mydb = sq.connect(
    host="localhost",       
    user="cs101",   
    password="dataisfun",
    allow_local_infile=True
)

# create cursor
mycursor = mydb.cursor()
print("Connected to MySQL database successfully!")

# create database
mycursor.execute("CREATE DATABASE IF NOT EXISTS cookies;")

# define database and table name
db_name = "cookies"
table_name = "sales"

# select database
mycursor.execute(f"USE {db_name};")

# create table
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Sales_Date VarChar(255),
    Day_of_Week VarChar(255),
    Salesman VarChar(255),
    Temperature FLOAT,
    Tweets FLOAT,
    Price FLOAT,
    Sales FLOAT
);
"""

# execute query
mycursor.execute(create_table_query)
print(f"Table '{table_name}' created or already exists.")

# define path to csv file 
csv_file_path = '/Users/kt/Harvard/CS101/Modules/Module4/Cookies Sample.csv'

# load data from csv into table
load_data_query = f"""
LOAD DATA LOCAL INFILE '{csv_file_path}'
INTO TABLE {table_name}
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Sales_Date, Day_of_Week, Salesman, Temperature, Tweets, Price, Sales);
"""

# execute query
try:
    mycursor.execute(load_data_query)
    mydb.commit()
    print(f"Successfully loaded data from {csv_file_path} into {table_name}.")
except sq.Error as err:
    print(f"MySQL Error: {err}")

# close connection
finally:
    mycursor.close()
    mydb.close()
