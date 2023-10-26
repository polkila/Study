# https://github.com/polkila/Study/blob/main/358203/Lesson10.py
import pandas as pd


import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)


# 1
def get_doomies(l):
    return {cat: [1 if i==cat else 0 for i in l] for cat in set(l)}

data = pd.DataFrame(get_doomies(lst))
print(data.head())


# 2
data = pd.DataFrame({'whoAmI':lst})
def to_doomies(dataframe, column_name):
    for i in set(dataframe[column_name]):
        dataframe[i] = 0
        dataframe.loc[dataframe[column_name]==i, i] = 1
    dataframe.drop(columns=column_name, inplace=True)
to_doomies(data, 'whoAmI')
print(data.head())