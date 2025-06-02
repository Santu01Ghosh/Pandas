import pandas as pd

newdata = {
    "FirstName" :['Ram','Shyam','Jodhu','Modhu','Abir','Souvik','Tamal','Anupam'],
    "Age":[22,24,23,15,23,21,25,28],
    "Salary":[55000,42152,74000,62000,25400,38247,65432,46000]
}

# creating dataframe :
df = pd.DataFrame(newdata)
print("Sample dataset")
print(df)

# for select one coloumn:
print("printing all name by selecting one column")
# If we select one column then it will return all the values of that column as a series
print(df["Age"])

# If we multiple column then it will return all the values of that column as a dataframe
print(df[['FirstName','Salary']])

