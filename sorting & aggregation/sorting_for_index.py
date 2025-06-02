import pandas as pd

data = {
    "Name": ["Tom", "Nick", "John"],
    "Age": [28,35,19],
    "Salary" : [10000,20000,30000]
}

df = pd.DataFrame(data)
print("Before Sorting :")
print(df)

df2 = df.sort_index(ascending=True)
print("After sorting :")
print(df2)
