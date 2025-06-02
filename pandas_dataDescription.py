import pandas as pd
# create some dataset 
newdata = {
    "FirstName" :['Ram','Shyam','Jodhu','Modhu','Abir','Souvik','Tamal','Anupam'],
    "Age":[22,24,23,15,23,21,25,28],
    "Salary":[55000,42152,74000,62000,25400,38247,65432,46000]
}

df = pd.DataFrame(newdata)
print(df)

print("Descriptive Statistics")
print(df.describe())