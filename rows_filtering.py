import pandas as pd

newdata = {
    "FirstName" :['Ram','Shyam','Jodhu','Modhu','Abir','Souvik','Tamal','Anupam'],
    "Age":[22,24,23,15,23,21,25,28],
    "Salary":[55000,42152,74000,62000,25400,38247,65432,46000]
}
df = pd.DataFrame(newdata)
print(df)

# Filtering rows where salary>50000
NewSalary = df[df['Salary']>50000]
# print(NewSalary)

print("Now time for multiple conditions by using &")
# filtering rows where Age>=22 and salary <=65000
newCon = df[(df['Age']>=22) & (df['Salary']<=65000)]
# print(newCon)


print("Now time for using | operation")
# filtering rows where Age>=22 OR salary <=45000
multiCon = df[(df['Age']>=22) | (df['Salary']<=45000)]
print(multiCon)