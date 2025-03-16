import pandas as pd  # Data processing
import numpy as np  # Handling NaN values

# Load data into a Pandas DataFrame
try: 
    df = pd.read_csv("cookies dirty data.csv")
except FileNotFoundError:   # Handle file not found error
    print("File not found")

# Display data types
print(df.dtypes)

# Remove empty rows where all values are missing
df.dropna(how="all", inplace=True)

# Remove duplicate rows to maintain unique records
df.drop_duplicates(inplace=True)

# Strip leading/trailing whitespace from categorical column
df["Salesman"] = df["Salesman"].str.strip()

# Clean 'Price' column: remove non-alphanumeric characters (keep only letters & numbers)
df['Price'] = df['Price'].replace(r'[^A-Za-z0-9]', np.nan, regex=True)

# Clean 'Tweets' and 'Sales' columns: remove non-alphanumeric characters (keep only letters & numbers)
df[['Tweets', 'Sales']] = df[['Tweets', 'Sales']].replace(r'[^A-Za-z0-9]', np.nan, regex=True)

# Convert 'Date' column to datetime format (MM/DD/YYYY)
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y', errors='coerce')

# Display the first few rows of the cleaned dataset
print(df.head())

# Save the cleaned dataset to a new CSV file, excluding index column
df.to_csv("cleanercookies.csv", index=False)
