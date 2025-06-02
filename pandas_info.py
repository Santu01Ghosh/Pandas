import pandas as pd
df = pd.read_json("D:\Pandas\sample_Data.json")
#Print a concise summary of a DataFrame
print("Displaying the information of dataframe")
# print(df.info())

# create our own dataframe :

datas = {
    "std_name" : ['Rittima','Sneha','Ankita'],
    "Marks" : [90,85,95],
    "Age" : [20,21,19],
    "Grade1" :['A','A+','B']
}
df = pd.DataFrame(datas)
print(df.info())