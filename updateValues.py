import pandas as pd

newdata = {
    "FirstName" :['Ram','Shyam','Jodhu','Modhu','Abir','Souvik','Tamal','Anupam'],
    "Age":[22,24,23,15,23,21,25,28],
    "Salary":[55000,42152,74000,62000,25400,38247,65432,46000],
    "Performance_score":[85,95,75,80,90,74,95,85]
}
df = pd.DataFrame(newdata)
print(df)


# add column "Country" --
df['Country'] = "India"
print(df)


# for accessing any specific cell and for further updation we've to use .loc() method
# df.loc[row_index,"Column name"] = new value
df.loc[1,'Salary'] = 45000
print(df)

# change Tamal's country -- 
df.loc[6,'Country'] = "South Korea"
print(df)