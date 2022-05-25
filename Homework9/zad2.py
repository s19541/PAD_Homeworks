import pandas as pd
import plotly.express as px
import scipy.stats as stats
import numpy as np
import statsmodels.formula.api as smf

PATH='Homework9/PAD_09_PD.csv'

df=pd.read_csv(PATH,sep=";")
df.rename(columns = {'Spending Score (1-100)':'Spending_score', 'Annual Income (k$)':'Annual_income'}, inplace = True)
model = smf.ols(formula="Spending_score ~ Gender + Age + Annual_income", data=df).fit()

#print(model.summary())
print('P Values: ', model.pvalues.values)
print('Coef: ', model.params.values)
print("Std Errs", model.bse.values)

px.scatter(df, "Age", "Spending_score", "Gender" , title = "Spending Score with Age and Gender").show()
px.scatter(df, "Age", "Annual_income", "Gender",  title = "Annual Income with Age and Gender").show()
px.scatter(df, "Annual_income", "Spending_score" , "Age",  title = "Spending Score with Age and Annual Income").show()
px.scatter(df, "Annual_income","Spending_score",  "Gender",  title = "Spending Score with Gender and Annual Income").show()

# Na podstawie wykresów i podsumopwania modelu można stwierdzić, że najmniejszy wpływ ma Płeć
model = smf.ols(formula="Spending_score ~ Age + Annual_income", data=df).fit()
print(model.summary())