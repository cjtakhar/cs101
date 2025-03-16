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

# Clean 'Price' column: remove non-numeric characters, keep numbers and decimals
df['Price'] = df['Price'].astype(str).str.replace(r'[^\d.]', '', regex=True)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')  # Convert cleaned text to numeric format

# Clean 'Tweets' and 'Sales' columns: remove non-numeric characters, keep numbers and decimals
df['Tweets'] = df['Tweets'].astype(str).str.replace(r'[^\d.]', '', regex=True)
df['Sales'] = df['Sales'].astype(str).str.replace(r'[^\d.]', '', regex=True)

# Convert 'Date' column to a standard datetime format (automatically detects format)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Display the first few rows of the cleaned dataset
print(df.head())

# Save the cleaned dataset to a new CSV file, excluding index column
df.to_csv("cleanercookies_best.csv", index=False)

