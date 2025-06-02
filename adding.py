# adding column
import pandas as pd

newdata = {
    "FirstName" :['Ram','Shyam','Jodhu','Modhu','Abir','Souvik','Tamal','Anupam'],
    "Age":[22,24,23,15,23,21,25,28],
    "Salary":[55000,42152,74000,62000,25400,38247,65432,46000],
    "Performance_score":[85,95,75,80,90,74,95,85]
}
df = pd.DataFrame(newdata)
print(df)

# adding columns('Bonus') by using assignment operator
df['Bonus'] = df['Salary']*0.2
df['Country'] = 'India'
print(df)

#adding column using insert() method---Main method used in professional setting
# df.insert(loc,column_name,some_data)
# creating a "Employee Id" column at first of the dataframe:
df.insert(0,"Employee ID",['E1','E2','E3','E4','E5','E6','E7','E8'])
print(df)

