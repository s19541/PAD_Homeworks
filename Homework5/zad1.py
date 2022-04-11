import pandas as pd
import datetime

PATH='Homework5/orders.csv'

df=pd.read_csv(PATH)
print('Before:')
print('Info :\n', df.info())
print('\nDescribe :\n', df.describe())
print('\nHead :\n', df.head(5))

# a)
df['order_date']=pd.to_datetime(df['order_date'], format='%Y/%m/%d')
# b)
print('\nUnique categories of tshirt :\n', df['tshirt_category'].value_counts())
# c)
df['tshirt_category']=df['tshirt_category'].astype(str)
df['tshirt_category']=df['tshirt_category'].apply(lambda x: x.replace('Wh ','White '))
df['tshirt_category']=df['tshirt_category'].apply(lambda x: x.replace('Bl ','Black '))
df['tshirt_category']=df['tshirt_category'].apply(lambda x: x.replace('Tshirt ','T-Shirt '))
# d)
def get_type_from_category(category: str):
    spliited_string = category.split()
    if len(spliited_string) == 1:
        return spliited_string[0]
    else:
        return spliited_string[1]

def get_colour_from_category(category: str):
    spliited_string = category.split()
    if len(spliited_string) == 1:
        return 'no_data'
    else:
        return spliited_string[0]

def get_size_from_category(category: str):
    spliited_string = category.split()
    if len(spliited_string) < 3:
        return 'no_data'
    else:
        return spliited_string[2]

df['tshirt_type']=df['tshirt_category'].apply(lambda x: get_type_from_category(x))
df['tshirt_colour']=df['tshirt_category'].apply(lambda x: get_colour_from_category(x))
df['tshirt_size']=df['tshirt_category'].apply(lambda x: get_size_from_category(x))
# f)
#print(df.where(df.loc[df['order_date'].between(datetime.date(2014, 12, 31), datetime.date(2016, 8, 2))]))
