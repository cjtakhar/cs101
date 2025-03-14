import mysql.connector as sq

# connect to mysql
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
mycursor.execute("CREATE DATABASE IF NOT EXISTS nj_state_teachers_salaries;")

# define database
db_name = "nj_state_teachers_salaries"

# define table name
table_name = "teachers_salaries"

# select database
mycursor.execute(f"USE {db_name};")

create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(255),
    first_name VARCHAR(255),
    county VARCHAR(255),
    district VARCHAR(255),
    school VARCHAR(255),
    primary_job VARCHAR(255),
    fte FLOAT,
    salary INT,
    certificate VARCHAR(255),
    subcategory VARCHAR(255),
    teaching_route VARCHAR(255),
    highly_qualified VARCHAR(255),
    experience_district INT,
    experience_nj INT,
    experience_total INT
);
"""
# execute query
mycursor.execute(create_table_query)

print(f"Table '{table_name}' created or already exists.")

# define path to csv file
csv_file_path = '/nj_teachers_salaries_pset3.csv'

# load data from csv into table
load_data_query = f"""
LOAD DATA LOCAL INFILE '{csv_file_path}'
INTO TABLE {table_name}
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '\\\\'
LINES TERMINATED BY '\n'
"""

# execute query
mycursor.execute(load_data_query)

print(f"Data loaded into '{table_name}' table.")

# commit changes
mydb.commit()

# close cursor and connection
mycursor.close()
mydb.close()

print("MySQL connection closed.")