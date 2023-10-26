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
def to_doomies(dataframe, src_column):
    for dst_column in set(dataframe[src_column]):
        dataframe[dst_column] = 0
        dataframe.loc[dataframe[src_column]==dst_column, dst_column] = 1
    dataframe.drop(columns=src_column, inplace=True)

data = pd.DataFrame({'whoAmI':lst})
to_doomies(data, 'whoAmI')
print(data.head())