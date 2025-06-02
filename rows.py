import pandas as pd

# head() & tail()
# head()--method returns the headers and a specified number of rows, starting from the top.

df = pd.read_csv("D:\Pandas\sales_data_sample.csv",encoding="latin1" )
# print(df.head(8)) #if the number of rows is not specified, the head() method will return the top 5 rows.
# print(df.head()) #if the number of rows is not specified, the head() method will return the top 5 rows.

# tail()--method for viewing the last rows of the DataFrame.
print(df.tail(10))
print(df.tail())