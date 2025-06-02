import pandas as pd

newdata = {
    "FirstName" :['Ram','Shyam','Jodhu','Modhu','Abir','Souvik','Tamal','Anupam'],
    "Age":[22,24,23,15,23,21,25,28],
    "Salary":[55000,42152,74000,62000,25400,38247,65432,46000],
    "Performance_score":[85,95,75,80,90,74,95,85]
}
df = pd.DataFrame(newdata)
print(df)

df['Salary'] = df['Salary']*1.05 # Update all salary
df.loc[4,'Age']=25 # update Abir's Age
print(df)

# for updating any particular cell we've to use .loc[] and for updating all value we can use assignment method.

