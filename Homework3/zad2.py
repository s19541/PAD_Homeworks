import pandas as pd

PATH='Homework3/PAD_03_PD.csv'

df=pd.read_csv(PATH,sep=";")
df.dropna()

df['owned_goods'] = df.apply(lambda row: row.owns_car + row.owns_TV + row.owns_house + row.owns_Phone, axis=1)

print(df)