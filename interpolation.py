import pandas as pd

tempdata = {
    "Day":['Mon','Tue','Wed','Thu','Fri','Sat'],
    "Temp":[30,None,32,38,None,42]
}

df = pd.DataFrame(tempdata)

# checking for missing values
print(df.isnull().sum())

print("Before interpolation :")
print(df)
# filing these missing values using interpolation -- 
# linear interpolation--
linear_df = df.copy()
linear_df['Temp'] = linear_df['Temp'].interpolate(method='linear')
# print("After interpolation :")
# print(linear_df)

# index interpolation----
index_df = df.copy()
index_df['Temp'] = index_df['Temp'].interpolate(method='index')
# print("After interpolation :")
# print(index_df)

# pad interpolation----
pad_df = df.copy()
pad_df['Temp'] = pad_df['Temp'].interpolate(method='pad')
# print("After interpolation :")
# print(pad_df)

# bfill interpolation
bfill_df = df.copy()
bfill_df['Temp'] = bfill_df['Temp'].interpolate(method='bfill')
# print("After interpolation :")
# print(bfill_df)


