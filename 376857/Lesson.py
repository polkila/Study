from math import factorial

def combinations(n, k):
    return factorial(n) / (factorial(k)*factorial(n-k))


# 1a
m = combinations(13, 4)
n = combinations(52, 4)
PA = m/n
print(PA) # 0.002641


# 1b
m = 0
for i in range(1,5):
    m += combinations(4, i) * combinations(48, 4-i)
n = combinations(52, 4)
PA = m/n
print(PA) # 0.28126


# 2
m = 1
n = combinations(10, 3)
PA = m/n
print(PA) # 0.00833


# 3
m = combinations(9, 3)
n = combinations(15, 3)
PA = m/n
print(PA) # 0.184615


# 4
m = 1
n = combinations(100, 2)
PA = m/n
print(PA) # 0.0002
