import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load Excel data
file_path = "SuperCookiesStore.xlsx"  # Replace if needed
excel_data = pd.ExcelFile(file_path)
store_df = excel_data.parse('SuperCookies Store')

# 🚿 CLEANING STARTS HERE 🚿

# 1. Rename columns for consistency
store_df.columns = store_df.columns.str.strip().str.replace(' ', '_').str.replace('-', '_')

# 2. Convert date column
store_df['Sales_Date'] = pd.to_datetime(store_df['Sales_Date'], errors='coerce')

# 3. Convert numeric columns
numeric_cols = ['Temperature', 'Tweets', 'Cost_of_Good_Sold', 'Price', 'Sales', 'Profit']
store_df[numeric_cols] = store_df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# 4. Drop rows with missing values in critical fields
store_df.dropna(subset=['Sales_Date', 'Sales', 'Profit'], inplace=True)

# 5. Filter out unrealistic values
store_df = store_df[(store_df['Sales'] >= 0) & (store_df['Profit'] >= 0)]

# 6. Add calculated field
store_df['Profit_per_Sale'] = store_df['Profit'] / store_df['Sales']

# 7. Save cleaned data to a new Excel file
store_df.to_excel("cleansupercookiesstore.xlsx", index=False)

print("✅ Cleaned data saved as 'cleansupercookiesstore.xlsx'")
