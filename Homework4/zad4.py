import pandas as pd

PATH='Homework4/zadanie_4.csv'

df=pd.read_csv(PATH,sep=";")
df.dropna(how='all', axis=1, inplace=True)
'''
min_times = df.groupby([pd.DatetimeIndex(df['DateTime']).normalize(), 'DoctorID', 'Type', 'City'])['DateTime'].min()
max_times = df.groupby([pd.DatetimeIndex(df['DateTime']).normalize(), 'DoctorID', 'Type', 'City'])['DateTime'].max()
print(min_times)
formatted_df = pd.merge(min_times, max_times, how='left', on=['DoctorID', 'Type', 'City', 'DateTime'])
formatted_df = formatted_df.rename(columns = {'DateTime_x': 'From', 'DateTime_y': 'To'}, inplace = False)
print(formatted_df)
'''
df = df.groupby([pd.DatetimeIndex(df['DateTime']).normalize(), 'DoctorID', 'Type', 'City']).agg({'DateTime' : ['min', 'max']})
print(df)
df.columns.droplevel(0)
df.columns = ["_".join(x) for x in df.columns.ravel()]

df = df.rename(columns = {'DateTime_min': 'From', 'DateTime_max': 'To'}, inplace = False)
print(df)
df.to_csv('Homework4/output4.csv', index=True)