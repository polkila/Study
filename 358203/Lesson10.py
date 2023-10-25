# 
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = {
    'robot': [1 if i=='robot' else 0 for i in lst],
    'human': [1 if i=='human' else 0 for i in lst],
}
data = pd.DataFrame(data)
data.head()