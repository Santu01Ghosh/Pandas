import pandas as pd

# Create a DataFrame by own -- 
data = {
    "Name" : ['Rohit','Santu','Sneha'],
    "Age" : [10,20,30],
    "city" : ['delhi','mumbai','pune']
}

df = pd.DataFrame(data)
print(df)

# how to save 
# df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)