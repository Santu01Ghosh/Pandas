import pandas as pd 

# customer dataframe
df_customers=pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':['Ramesh','Suresh','Kalpesh']
})

#order dataframe
df_orders = pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrederAmount':[350,1120,985]
})

df_merged = pd.merge(df_customers,df_orders, on="CustomerID",how="inner")
print("Inner join :")
print(df_merged)

df_merged = pd.merge(df_customers,df_orders, on="CustomerID",how="left")
print("Left join :")
print(df_merged)

df_merged = pd.merge(df_customers,df_orders, on="CustomerID",how="right")
print("Right join :")
print(df_merged)

df_merged = pd.merge(df_customers,df_orders, on="CustomerID",how="outer")
print("Outer join :")
print(df_merged)