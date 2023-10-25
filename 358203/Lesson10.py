# https://github.com/polkila/Study/blob/main/358203/Lesson10.py
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

def get_doomies(l):
    return {cat: [1 if i==cat else 0 for i in l] for cat in list(set(l))}

print(get_doomies(lst))