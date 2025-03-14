import mysql.connector as sq
import os

# Define CSV file path
csv_file_path = '/var/lib/mysql-files/monthly_revenue.csv'

# Check if file exists
if not os.path.exists(csv_file_path):
    print("❌ CSV file not found!")
    exit()

# Connect to MySQL
mydb = sq.connect(
    host="localhost",
    user="cs101",
    password="dataisfun",
    allow_local_infile=True
)
mycursor = mydb.cursor()
print("Connected to MySQL server!")

# Create database if it doesn't exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS monthly_revenue")

# Select database
mycursor.execute("USE monthly_revenue") 

# Create table with correct data types
create_table_query = """
CREATE TABLE IF NOT EXISTS revenue (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Date DATE,
    Land_Class VARCHAR(255),
    Land_Category VARCHAR(255),
    State VARCHAR(255),
    County VARCHAR(255),
    FIPS_Code VARCHAR(10),  
    Offshore_Region VARCHAR(255),
    Revenue_Type VARCHAR(255),
    Mineral_Lease_Type VARCHAR(255),
    Commodity VARCHAR(255),
    Product VARCHAR(255),
    Revenue DECIMAL(15,2)
);
"""

# Execute query
mycursor.execute(create_table_query)
print("✅ Table 'revenue' created or already exists.")

# Load data into MySQL
load_data_query = f"""
LOAD DATA LOCAL INFILE '{csv_file_path}'
INTO TABLE revenue
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Date, Land_Class, Land_Category, State, County, FIPS_Code, Offshore_Region, Revenue_Type, Mineral_Lease_Type, Commodity, Product, Revenue);
"""

try:
    mycursor.execute(load_data_query)
    mydb.commit()
    print("✅ Data loaded into table 'revenue' successfully!")
except Exception as e:
    print(f"❌ Error loading data: {e}")

# Close connections
mycursor.close()
mydb.close()
print("✅ Database connection closed.")
