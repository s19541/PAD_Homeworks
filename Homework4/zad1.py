import pandas as pd

PATH='Homework4/Zadanie_1.csv'

df=pd.read_csv(PATH,sep=";")
df.dropna()