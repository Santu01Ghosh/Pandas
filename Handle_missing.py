import pandas as pd
newdata = {
    "FirstName" :['Ram','Shyam',None,'Modhu','Abir','Souvik','Tamal','Anupam'],
    "Age":[22,24,None,15,23,21,25,28],
    "Salary":[55000,42152,None,62000,25400,38247,65432,46000],
    "Performance_score":[85,95,None,80,90,74,95,85]

}
df = pd.DataFrame(newdata)
print(df)

# for handling missing data pandas has one method which is .dropna()
# syntax - df.dropna(inplace=True) --this method will drop the rows & columns which contains missing values
# df.dropna(axis=0,inplace = True) -- it(axis=0) works only for rows
# df.dropna(axis=1,inplace = True) -- it(axis=1) works only for columns
print("Cheking missing values :")
print(df.isnull().sum()) # for checking missing values

print("After removing all missing values :")
df.dropna(axis =0,inplace=True)
print(df)