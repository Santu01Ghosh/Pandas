""" Aggregation in Pandas
Aggregation means applying a mathematical function to summarize data. It can be used to get a summary of columns in our dataset like getting sum, minimum, maximum etc. from a particular column of our dataset. The function used for aggregation is agg() the parameter is the function we want to perform. Some functions used in the aggregation are:

sum()         : Compute sum of column values
min()          : Compute min of column values
max()         : Compute max of column values
mean()       : Compute mean of column
size()          : Compute column sizes
describe()  : Generates descriptive statistics
first()          : Compute first of group values
last()          : Compute last of group values
count()       : Compute count of column values
std()           : Standard deviation of column
var()           : Compute variance of column
sem()         : Standard error of the mean of column
"""

import pandas as pd
data = {
    "Name": ["Tom", "Nick", "John"],
    "Age": [28,35,19],
    "Salary" : [10000,20000,30000]
}
df = pd.DataFrame(data)
print(df)

# finding average salary :
avg_salary = df['Salary'].mean()
print(avg_salary)

min_salary = df['Salary'].min()
print(min_salary)


max_salary = df['Salary'].max()
print(max_salary)

count_name = df['Name'].count()
print(count_name)