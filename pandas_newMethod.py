import pandas as pd

newdata = pd.DataFrame({
    "FirstName" :['Ram','Shyam','Jodhu','Modhu','Abir','Souvik','Tamal','Anupam'],
    "Age":[22,24,23,15,23,21,25,28],
    "Salary":[55000,42152,74000,62000,25400,38247,65432,46000]
})
print(newdata)

# An f-string lets you embed variables or expressions directly inside a string using curly braces {}.
print(f'Shape: {newdata.shape}')
print(f'Column names :{newdata.columns}')