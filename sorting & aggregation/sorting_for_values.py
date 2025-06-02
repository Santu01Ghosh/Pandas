# What is Sorting in Pandas?
# Sorting means arranging data in ascending or descending order by values in one or more columns.

# Pandas provides:

# sort_values() — Sort by column values

# sort_index() — Sort by row index

# syntax---
# df.sort_values(by="Column_name", ascending=True/False, inplace = True)


import pandas as pd

data = {
    "Name": ["Tom", "Nick", "John"],
    "Age": [28,35,19],
    "Salary" : [10000,20000,30000]
}

df = pd.DataFrame(data)
print("Before Sorting :")
print(df)

# target single column
# df.sort_values(by = 'Age', ascending=False, inplace=True) # in decending order bcz ascending  = False
# print("After Sorting :")
# print(df)

# target multiple columns -- 
df.sort_values(by = ["Name","Salary"],ascending=[True,False],inplace=True)
print("After Sorting :")
print(df)

