import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the data
file_path = '/Users/kt/Harvard/CS101/StudyPack/practice/sf_housing.csv'
data = pd.read_csv(file_path)

# Convert all column names to lowercase immediately
data.columns = data.columns.str.lower()

# Display initial data info
print("Initial Data Types:\n", data.info())
print("\nFirst 5 Rows Before Cleaning:\n", data.head())

# Convert 'observation_date' to datetime format
data['observation_date'] = pd.to_datetime(data['observation_date'], errors='coerce')

# Drop rows with missing values in 'observation_date' and 'sfxrsa'
data.dropna(subset=['observation_date', 'sfxrsa'], inplace=True)

# Reset index after dropping rows
data.reset_index(drop=True, inplace=True)

# Convert 'sfxrsa' to a numeric type
data['sfxrsa'] = pd.to_numeric(data['sfxrsa'], errors='coerce')

# Display the number of missing values
print("\nMissing Values After Cleaning:\n", data.isnull().sum())

# Display final data types
print("\nFinal Data Types:\n", data.dtypes)
print("\nFirst 5 Rows After Cleaning:\n", data.head())

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(data['observation_date'], data['sfxrsa'], marker='o', linestyle='-')
plt.xlabel('Year')
plt.ylabel('Housing Price Index (SFXRSA)')
plt.title('San Francisco Housing Price Index Over Time')
plt.grid(True)
plt.show()
