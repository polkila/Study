# https://github.com/polkila/Study/blob/main/358203/Lesson10.py
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
cats = list(set(lst))
table = {}
for cat in cats:
    table[cat] = [1 if i==cat else 0 for i in lst]
data = pd.DataFrame(table)
data.head()