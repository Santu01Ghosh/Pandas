# for handling the missing data's we need to learn some topic --
"""NaN(not a number)
None(for object data types)

for checking where value is missing we've to use - 
isnull()
True - Nan
False- not Nan
"""
import pandas as pd
newdata = {
    "FirstName" :['Ram','Shyam',None,'Modhu','Abir','Souvik','Tamal','Anupam'],
    "Age":[22,24,None,15,23,21,25,28],
    "Salary":[55000,42152,None,62000,25400,38247,65432,46000],
    "Performance_score":[85,95,None,80,90,74,95,85]

}
df = pd.DataFrame(newdata)
print(df)

# for checking where value is missing we've to use -
print(df.isnull())
# for checking all insights related to missing data--
print(df.isnull().sum()) 