import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Excel data
file_path = "SuperCookiesStore.xlsx"  # Replace with your file name if different
excel_data = pd.ExcelFile(file_path)
store_df = excel_data.parse('SuperCookies Store')

# Filter data for Ada
ada_df = store_df[store_df['Salesclerk'] == 'Ada'].copy()
ada_df['Sales_Date'] = pd.to_datetime(ada_df['Sales_Date'])

# Chart 1: Distribution of Ada's Sales (Histogram)
plt.figure(figsize=(8, 6))
sns.histplot(ada_df['Sales'], bins=10, kde=True)
plt.title("Distribution of Units Sold by Ada")
plt.xlabel("Units Sold")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Chart 2: Effect of Ada's Tweets on Sales (Scatter with Trendline)
plt.figure(figsize=(8, 6))
sns.regplot(x='Tweets', y='Sales', data=ada_df)
plt.title("Effect of Ada's Tweets on Sales")
plt.xlabel("Number of Tweets")
plt.ylabel("Units Sold")
plt.grid(True)
plt.show()

# Chart 3: Ada's Profit Per Sale Over Time (Bar Plot)
ada_df['Profit_per_Sale'] = ada_df['Profit'] / ada_df['Sales']
plt.figure(figsize=(8, 6))
sns.barplot(x=ada_df['Sales_Date'].dt.strftime('%Y-%m-%d'), y='Profit_per_Sale', data=ada_df)
plt.xticks(rotation=90)
plt.title("Ada's Profit Per Sale Over Time")
plt.xlabel("Date")
plt.ylabel("Profit per Sale")
plt.grid(True)
plt.tight_layout()
plt.show()

# Chart 4: Ada's Profit vs Cost of Goods Sold (Scatter)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Cost of Good Sold', y='Profit', data=ada_df)
plt.title("Ada's Profit vs Cost of Goods Sold")
plt.xlabel("Cost of Goods Sold")
plt.ylabel("Profit")
plt.grid(True)
plt.show()