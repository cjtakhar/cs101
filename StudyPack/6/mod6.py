import pandas as pd
import numpy as np

# Load the CSV file
file_path = "Cookies dirty data.csv"
df = pd.read_csv(file_path, parse_dates=["Date"])

# Drop rows where all values are NaN
df.dropna(how="all", inplace=True)

# Strip leading and trailing spaces from Salesman column
df["Salesman"] = df["Salesman"].str.strip()

# Replace non-numeric characters in "Price" with NaN
df["Price"] = df["Price"].replace(r'[^0-9.]', np.NaN, regex=True)

# Ensure "Tweets" and "Price" contain only numeric values
df[["Tweets", "Price"]] = df[["Tweets", "Price"]].replace(r'[^0-9]', np.NaN, regex=True)

# Convert "Sales" and "Tweets" to numeric, coercing errors
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Tweets"] = pd.to_numeric(df["Tweets"], errors="coerce")

# Drop rows with any NaN values after processing
df.dropna(inplace=True)

# Print unique values before filtering to debug
print("Unique Salesmen before filtering:", df["Salesman"].unique())

# Save cleaned data
df.to_csv("Cookies_cleaned_data.csv", index=False)

# Filtering

print("Ada's sales before filtering:")
print(df[df["Salesman"] == "Ada"])

df_filter = df["Salesman"] == "Ada"
df_filtered_ada = df[df_filter]

df_filter = (df["Salesman"] == "Ada") & (df["Day"] == "Monday")
df_filtered_ada_monday = df[df_filter]

df_filter = (df["Day"] == "Monday") | (df["Day"] == "Tuesday")
df_filtered_monday_tuesday = df[df_filter]

df_filter = (df["Sales"] >= 100) & (df["Tweets"] <= 1)
df_filtered_sales_tweets = df[df_filter]

print("Ada's sales after filtering:")
print(df_filtered_sales_tweets[df_filtered_sales_tweets["Salesman"] == "Ada"])


# Print unique Salesmen after filtering
print("Unique Salesmen after filtering:", df_filtered_sales_tweets["Salesman"].unique())

# Save filtered data
df_filtered_sales_tweets.to_csv("cookies_filtered.csv", index=False)

# Create a separate DataFrame for pivoting to avoid index issues
df_pivot_data = df_filtered_sales_tweets.copy()

# Pivot Tables (keep Date as a column)
df_pivot1 = df_pivot_data.pivot_table(index="Date", columns="Salesman", values="Sales", aggfunc="sum")  # Sum Sales
df_pivot2 = df_pivot_data.pivot_table(index="Date", columns="Salesman", values="Sales", aggfunc="mean")  # Mean Sales
df_pivot_table = df_pivot_data.pivot_table(index="Salesman", columns="Date", values="Sales", aggfunc="sum")  # Salesman as index

# Fill NaN values with 0 before saving
df_pivot1.fillna(0, inplace=True)
df_pivot2.fillna(0, inplace=True)
df_pivot_table.fillna(0, inplace=True)

# Save pivot table data
df_pivot1.to_csv("cookies_pivot_table_sum.csv", index=True)
df_pivot2.to_csv("cookies_pivot_table_mean.csv", index=True)
df_pivot_table.to_csv("cookies_pivot_table.csv", index=True)

print("Pivot tables saved successfully.")
