"""
Grouping in Pandas
Grouping in Pandas means organizing your data into groups based on some columns. Once grouped you can perform actions like finding the total, average, count or even pick the first row from each group. This method follows a split-apply-combine process:

Split the data into groups
Apply some calculation like sum, average etc.
Combine the results into a new table.


"""

import pandas as pd
data = {
    "Item" : ['Cake','Cake','Bread','Pastry','Cake' ],
    "Flavor" : ['Chocolate','Vanilla','Whole Wheat','Stawberry','Chocolate'],
    "Price" : [250,220,80,120,250]
}

df = pd.DataFrame(data)
print(df)

# grouping data by one column :
gropued = df.groupby('Item') # it just creates a grouped object
print(gropued)

print(df.groupby('Item')['Price'].sum())

print("Muultiple group by :----")
print(df.groupby(['Item','Flavor'])['Price'].sum())