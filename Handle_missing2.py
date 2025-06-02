import pandas as pd
newdata = {
    "FirstName" :['Ram','Shyam','Jodu','Modhu','Abir','Souvik','Tamal','Anupam'],
    "Age":[22,24,None,15,23,21,25,28],
    "Salary":[55000,42152,None,62000,25400,38247,65432,46000],
    "Performance_score":[85,95,None,80,90,74,95,85]

}
df = pd.DataFrame(newdata)
print(df)
print("Cheking for missing values in the dataframe:")
print(df.isnull().sum())
# in some cases instead of removing the NaN values, we can replace the value with a specific value by using .fillna() method

# if we want to fill all NaN values with some particular value -- sytax -- df.fillna(value,iplace=True)
# df.fillna(0,inplace=True)
# print(df)
# print(df.isnull().sum())      # now no NaN values are present in the dataframe.  
# we can also fill NaN values with mathrmatical terms like mean, median, mode etc. by using .fillna() method, because filling value with any particular value cause some inappropriate results in the dataframe.

df['Age']=df['Age'].fillna(df['Age'].mean())
df['Salary']=df['Salary'].fillna(df['Salary'].mean())
df['Performance_score']=df['Performance_score'].fillna(df['Performance_score'].mean())
print("After filling all the data using .fillna() -- ")
print(df)