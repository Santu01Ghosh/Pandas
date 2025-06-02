import pandas as pd


#use to_string() to print the entire DataFrame.
# read data from CSV file into a dataframe
# df = pd.read_csv("D:\Pandas\sales_data_sample.csv",encoding = "latin1")

# read data from excel file into a dataframe
# df = pd.read_excel(r"D:\Pandas\SampleSuperstore.xlsx", engine='openpyxl')

#read data from json file into a dataframe
df = pd.read_json("D:\Pandas\sample_Data.json")
print(df)

