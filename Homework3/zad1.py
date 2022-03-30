import pandas as pd

PATH='Homework3/PAD_03_PD.csv'

df=pd.read_csv(PATH,sep=";")
df.dropna()
print(df['Country'].value_counts())