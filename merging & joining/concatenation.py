import pandas as pd

df_region1 = pd.DataFrame({
    'CustomerID':[1,2],
    'Name':['santu','kiara'] 
})

df_Region2 = pd.DataFrame({
    'CustomerID' : [3,4],
    'Name' : ['rittima','katrina']
})

df_concat = pd.concat([df_region1,df_Region2], ignore_index=True)
print(df_concat)