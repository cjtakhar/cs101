import pandas as pd
import numpy as np
import mysql.connector as sq

# Create a DataFrame
df = pd.read_csv('/Users/kt/Harvard/CS101/PSET/pset4/nj_teachers_salaries_pset4.csv')

#Display info
df.info()

# Drop rows that have all values as NaN
df.dropna(how="all", inplace=True)

# Identify numerical columns (excluding 'id')
numerical_columns = ['fte', 'salary', 'experience_district', 'experience_nj', 'experience_total']

# Replace non-numeric values with NaN
df[numerical_columns] = df[numerical_columns].replace(r'[^0-9.]', np.nan, regex=True)

# Drop rows with NaN values in any numerical column
df.dropna(subset=numerical_columns, inplace=True)

# Convert numerical columns to the correct types
df['fte'] = df['fte'].astype(float)  # Float
df['salary'] = df['salary'].astype(float)  # Float
df['experience_district'] = df['experience_district'].astype(float)  # Float
df['experience_nj'] = df['experience_nj'].astype(float)  # Float
df['experience_total'] = df['experience_total'].astype(float)  # Float

# Fill missing ID values with sequential numbers starting from max existing ID + 1
next_id = int(df['id'].max()) + 1
df.loc[df['id'].isna(), 'id'] = range(next_id, next_id + df['id'].isna().sum())

# Convert ID column to integer
df['id'] = df['id'].astype(int)

# Show a few examples of fixed rows
print("\nExamples of fixed 'id' values:")
print(df.loc[df['id'].isna()].head(5))  # Should return an empty DataFrame if all NaNs were fixed

# Final check to ensure no missing values in numerical columns
print("\nFinal Check: Any remaining NaNs in numerical columns?")
print(df[['id', 'fte', 'salary', 'experience_district', 'experience_nj', 'experience_total']].isna().sum())

# Identify string/object columns
string_columns = df.select_dtypes(include=['object']).columns

# Remove leading and trailing spaces from all string columns
df[string_columns] = df[string_columns].apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Show examples where spaces were removed
modified_names = df[
    (df['first_name'].str.startswith(' ')) | (df['first_name'].str.endswith(' ')) |
    (df['last_name'].str.startswith(' ')) | (df['last_name'].str.endswith(' '))
]

# Display a few modified rows
print("\nExamples where leading/trailing spaces were removed (first_name, last_name):")
print(modified_names[['first_name', 'last_name']].head(2))  # Show at least 2 examples

# Final check to confirm no rows were dropped
print("\nFinal Check: Number of rows before and after cleaning")
print(f"Original Row Count: {len(df)}")

# Identify string columns
string_columns = df.select_dtypes(include=['object']).columns

# Define valid character patterns for different string columns (using raw strings r"")
valid_patterns = {
    'primary_job': r"[^A-Za-z0-9\s&\-,/]",  # Letters, numbers, spaces, &, -, /
    'teaching_route': r"[^A-Za-z\s\-']",  # Letters, spaces, -, '
    'subcategory': r"[^A-Za-z\s\-,.:]",  # Letters, spaces, -, ., :
    'first_name': r"[^A-Za-z\-' ]",  # Letters, hyphens, and apostrophes
    'last_name': r"[^A-Za-z\-' ]"  # Letters, hyphens, and apostrophes
}

# Apply regex cleaning to respective columns
for col, pattern in valid_patterns.items():
    df[col] = df[col].str.replace(pattern, '', regex=True)

# Identify modified rows
modified_rows = df[string_columns].copy()
for col in valid_patterns.keys():
    modified_rows[col] = df[col] != df[col].str.replace(valid_patterns[col], '', regex=True)

# Show examples of modified rows
modified_rows = df[modified_rows.any(axis=1)]

# Display a few examples of modified rows
print("\nExamples of modified string column values:")
print(modified_rows[['primary_job', 'teaching_route', 'subcategory', 'first_name', 'last_name']].head(5))

# Final row count check to ensure minimal data loss
print("\n Final Check: Number of rows before and after cleaning")
print(f"Row count after Question 3: {len(df)}")

# Save the cleaned dataframe as 'cleaned_data.csv'
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned data has been successfully saved as 'cleaned_data.csv'.")

# MySQL connection
mydb = sq.connect(
    host="localhost", 
    user="cs101",
    password="dataisfun"
)

# Create a cursor object
mycursor = mydb.cursor()

# Create the database if it doesn't exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS nj_state_teachers_salaries")

# Use the database
mycursor.execute("USE nj_state_teachers_salaries")

# Drop table if it already exists to avoid conflicts
mycursor.execute("DROP TABLE IF EXISTS teachers_salaries_pset4")

# Create table with appropriate data types
create_table_query = """
CREATE TABLE teachers_salaries_pset4 (
    id INT PRIMARY KEY,
    last_name VARCHAR(50),
    first_name VARCHAR(50),
    county VARCHAR(50),
    district VARCHAR(100),
    school VARCHAR(100),
    primary_job VARCHAR(150),
    fte FLOAT,  -- Float data type
    salary FLOAT,  -- Float data type
    certificate VARCHAR(50),
    subcategory VARCHAR(50),
    teaching_route VARCHAR(50),
    highly_qualified VARCHAR(100),
    experience_district FLOAT,  -- Float because we kept decimals
    experience_nj FLOAT,  -- Float because we kept decimals
    experience_total FLOAT  -- Float because we kept decimals
);
"""
# Execute the table creation query
mycursor.execute(create_table_query)

print("\nTable 'teachers_salaries_pset4' created successfully.")

# Load data from cleaned_data.csv into the MySQL table
load_data_query = """
LOAD DATA INFILE '/Users/kt/Harvard/CS101/PSET/pset4/cleaned_data.csv' 
INTO TABLE teachers_salaries_pset4 
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS;
"""

# Execute the data loading query
mycursor.execute(load_data_query)

# Commit the changes
mydb.commit()

print("\nData loaded successfully into 'teachers_salaries_pset4'.")

cmd = "select count(*) from \
                 nj_state_teachers_salaries.teachers_salaries_pset4 "
mycursor.execute(cmd)
count = mycursor.fetchone()[0]

print(f"Number of rows in teachers_salaries table : {count}")

cmd = """SELECT COUNT(*) \
                FROM INFORMATION_SCHEMA.COLUMNS \
                WHERE table_schema = 'nj_state_teachers_salaries' \
                AND table_name = 'teachers_salaries_pset4'"""
mycursor.execute(cmd)
count = mycursor.fetchone()[0]
print(f"Number of columns in teachers_salaries table : {count}") 

df = pd.read_csv('/Users/kt/Harvard/CS101/PSET/pset4/sample.csv')

# Display the first 5 rows
print("First 5 rows:")
print(df.head(5))

# Display the last 5 rows
print("\nLast 5 rows:")
print(df.tail(5))

# Print the shape of the dataframe
print("\nShape of the dataframe:", df.shape)
