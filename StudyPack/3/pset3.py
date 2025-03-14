# grade 100/100

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
mycursor.execute("CREATE DATABASE IF NOT EXISTS nj_state_teachers_salaries;")

# define database and table name
db_name = "nj_state_teachers_salaries"
table_name = "teachers_salaries"

# select database
mycursor.execute(f"USE {db_name};")

# create table
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
mycursor.execute(create_table_query)
print(f"Table '{table_name}' created or already exists.")

# define path to csv file
csv_file_path = '/var/lib/mysql-files/nj_teachers_salaries_pset3.csv'

# load data from csv file into table
load_data_query = f"""
LOAD DATA LOCAL INFILE '{csv_file_path}'
INTO TABLE {table_name}
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"' 
ESCAPED BY '\\\\'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(last_name, first_name, county, district, school, primary_job,
fte, salary, certificate, subcategory, teaching_route,
highly_qualified, experience_district, experience_nj, experience_total);
"""

# execute load data query
try:
    mycursor.execute(load_data_query)
    mydb.commit()
    print(f"Successfully loaded data from {csv_file_path} into {table_name}.")
except sq.Error as err:
    print(f"MySQL Error: {err}")

    cmd = "select count(*) from \
                 nj_state_teachers_salaries.teachers_salaries"
mycursor.execute(cmd)
count = mycursor.fetchone()[0]

print(f"Number of rows in teachers_salaries table : {count}")

cmd = """SELECT COUNT(*) \
                FROM INFORMATION_SCHEMA.COLUMNS \
                WHERE table_schema = 'nj_state_teachers_salaries' \
                AND table_name = 'teachers_salaries'"""
mycursor.execute(cmd)
count = mycursor.fetchone()[0]
print(f"Number of columns in teachers_salaries table : {count}")