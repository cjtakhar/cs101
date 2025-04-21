import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Excel file
file_path = "SuperCookiesStore.xlsx"  # Replace with your file name
excel_data = pd.ExcelFile(file_path)
store_df = excel_data.parse('SuperCookies Store')

# Prepare Ada's data
ada_df = store_df[store_df['Salesclerk'] == 'Ada'].copy()
ada_df['Sales_Date'] = pd.to_datetime(ada_df['Sales_Date'])

# Chart 1: Sales Distribution by Salesclerk (Box Plot)
plt.figure(figsize=(10, 6))
sns.boxplot(x='Salesclerk', y='Sales', data=store_df)
plt.title("Sales Distribution by Salesclerk")
plt.xlabel("Salesclerk")
plt.ylabel("Units Sold")
plt.grid(True)
plt.show()

# Chart 2: Ada's Tweet Activity vs Profit (Regression)
plt.figure(figsize=(8, 6))
sns.regplot(x='Tweets', y='Profit', data=ada_df)
plt.title("Ada's Tweet Activity vs Profit")
plt.xlabel("Number of Tweets")
plt.ylabel("Profit")
plt.grid(True)
plt.show()

# Chart 3: Average Profit Per Sale by Salesclerk (Bar Plot)
store_df['Profit_per_Sale'] = store_df['Profit'] / store_df['Sales']
plt.figure(figsize=(8, 6))
sns.barplot(x='Salesclerk', y='Profit_per_Sale', data=store_df)
plt.title("Average Profit Per Sale by Salesclerk")
plt.xlabel("Salesclerk")
plt.ylabel("Profit per Sale")
plt.grid(True)
plt.show()

# Chart 4: Ada's Profit vs Temperature (Scatter with Trendline)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Temperature', y='Profit', data=ada_df)
sns.regplot(x='Temperature', y='Profit', data=ada_df, scatter=False, color='red')
plt.title("Ada's Profit vs Temperature")
plt.xlabel("Temperature (°F)")
plt.ylabel("Profit")
plt.grid(True)
plt.show()
