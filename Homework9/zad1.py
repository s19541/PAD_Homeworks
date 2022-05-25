import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
import numpy as np

PATH='Homework9/PAD_09_PD.csv'

df=pd.read_csv(PATH,sep=";")

male_incomes = df.loc[df['Gender'] == 'Male']['Annual Income (k$)'].tolist()
female_incomes = df.loc[df['Gender'] == 'Female']['Annual Income (k$)'].tolist()

#Poziom istotności = 0,05
#Hipoteza zerowa = Nie ma istotnej różnicy w średnich dochodach mężczyzn i kobiet
#Hipoteza alternatywna = Istnieje istotna różnica w średnich dochodach mężczyzn i kobiet

print(np.var(female_incomes), np.var(male_incomes))
#Stosunek wariancji większej próbki do mniejszej jest mniejszy od 4, więc można założyć, że wariancje są równe

print(stats.ttest_ind(a=female_incomes, b=male_incomes, equal_var=True))
# statistic=-0.795022298602198, pvalue=0.42755249399927864
# pvalue > poziomu istotności, więc nie można odrzucić hipotezy zerowej