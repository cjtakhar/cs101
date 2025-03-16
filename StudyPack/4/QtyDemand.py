import pandas as pd

df = pd.read_excel("./QtyDemandSP.xlsx")
# df = pd.read_excel("./QtyDemand.xlsx", usecols=["Sales", "Price"])
# print(df)

highest_sales = df[df["Sales"]>10]
print(highest_sales)

price = df["Price"]
print(price)

# df.to_excel("QtyDemandSP.xlsx", index=False)
# print("File created successfully")