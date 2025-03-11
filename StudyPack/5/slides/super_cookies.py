import mysql.connector as sq
import pandas as pd

# Connect to Database
mydb=sq.connect(host="localhost",user="cs101",passwd="dataisfun",buffered=True)

# Query the database and load into Pandas DataFrame
query = "SELECT * FROM sales"
df = pd.read_sql(query, engine)

# Print DataFrame
print(df)