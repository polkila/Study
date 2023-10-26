# https://github.com/polkila/Study/blob/main/358203/Lesson10.py
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# 1
def get_doomies(l):
    return {cat: [1 if i==cat else 0 for i in l] for cat in set(l)}

print(get_doomies(lst))

# 2
import pandas as pd
data = pd.DataFrame({'whoAmI':lst})
data['robot'] = 0
data.loc[data['whoAmI']=='robot', 'robot'] = 1
data['human'] = 0
data.loc[data['whoAmI']=='human', 'human'] = 1
data.drop(columns='whoAmI', inplace=True)
print(data.head())