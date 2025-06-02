import pandas as pd
newdata = {
    "FirstName" :['Ram','Shyam','Jodhu','Modhu','Abir','Souvik','Tamal','Anupam'],
    "Age":[22,24,23,15,23,21,25,28],
    "Salary":[55000,42152,74000,62000,25400,38247,65432,46000],
    "Performance_score":[85,95,75,80,90,74,95,85]

}
df = pd.DataFrame(newdata)
print(df)

# for removing any columns and row -- It keeps our data clean
# df.drop(columns = ["Column_name"],inplace =true)
# columns=[...]: Specifies the column(s) to drop
# .inplace=True: Directly modifies the original df.
# for removing multiple column syntax : df.drop(columns=['column1','column2','column3'],inplace=True)
print("Modified data :")
df.drop(columns=['Performance_score','Age'],inplace=True)
print(df)