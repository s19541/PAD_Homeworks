import pandas as pd

# zad 1
PATH='Homework5/orders.csv'

df=pd.read_csv(PATH)
print('Info :\n', df.info)
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
mask = (df['order_date'] > '31/12/2016') & (df['order_date'] <= '02/08/2016')
print(df.loc[mask])

# zad 2

PATH2='Homework5/customers.csv'

df2=pd.read_csv(PATH2)

# a)
print('\nColumns :\n', df2.columns)
# b)
print('Size of data from first exercise: ', df.size, df.shape)
print('Size of dataframe from second exercise: ', df2.size, df2.shape)

print('Size in memory of dataframe from first exercise: ' , df.memory_usage(index=True).sum(), ' bytes')
print('Size in memory of dataframe from second exercise: ', df2.memory_usage(index=True).sum(), ' bytes')
# c)
df2.rename(columns = {'customerID':'customer_id'}, inplace = True)
# d)
df_merged = df.merge(df2,on = 'customer_id')
print(df_merged)
'''
Do polączenia tych dwóch ramek użyłem funkcji merge, powodem mojego wyboru jest to, że ta funkcja pozwala na łączenie dwóch ramek na podstawie ich części wspólnej ( customer_id)
'''
# zad 3
df.to_csv('Homework5/output.csv', index=False)