import pandas as pd
import numpy as np

file_path = "Cookies dirty data.csv"

df = pd.read_csv(file_path, parse_dates=["Date"])

df.dropna(how="all", inplace=True)

df["Salesman"] = df["Salesman"].str.strip()

df["Price"] = df["Price"].replace('[^A-Za-z0-9]', np.NaN, regex=True)

df[["Tweets", "Price"]] = df[["Tweets", "Price"]].replace('[^0-9]', np.NaN, regex=True)

df.dropna()

df.to_csv("Cookiesceleanerdata.csv", index=False)