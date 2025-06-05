import pandas as pd

data = pd.read_csv("D:\Pandas\customers-100 (1).csv")
# print(data.info())
# print(data.isnull().sum())
# data.dropna("")
print(data)
duplicates = data[data.duplicated()]
print("\nDuplicate rows (all columns):")
print(duplicates)