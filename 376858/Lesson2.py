from math import factorial, pow 

def combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))

def Bernoulli(n, k, p):
    return combinations(n, k) * pow(p, k) * pow(1-p, n-k)

def Poisson(l, m):
    return pow(l, m) / factorial(m) * pow(2.72, -l)


# 1. Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. 
# Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
p = 0.8
n = 100
m = 85
Pm = Bernoulli(n, m, p)
print('1', Pm) # 0.04806


# 2. Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. 
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек. 
# a. Какова вероятность, что ни одна из них не перегорит в первый день? 
# b. Какова вероятность, что перегорят ровно две?
# 2a
p = 0.0004
n = 5000
l = p*n
m = 0
Pm = Poisson(l, m)
print('2a', Pm) # 0.135164
# 2b
p = 0.0004
n = 5000
l = p*n
m = 2
Pm = Poisson(l, m)
print('2b', Pm) # 0.2703


# 3. Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
p = 0.5
n = 144
m = 70
Pm = Bernoulli(n, m, p)
print('3', Pm) # 0.06281


# 4. В первом ящике находится 10 мячей, из которых 7 - белые. 
# Во втором ящике - 11 мячей, из которых 9 белых. 
# Из каждого ящика вытаскивают случайным образом по два мяча. 
# a. Какова вероятность того, что все мячи белые? 
# b. Какова вероятность того, что ровно два мяча белые? 
# c. Какова вероятность того, что хотя бы один мяч белый?
n1 = combinations(10, 2); n2 = combinations(11, 2);
def PA1xPA2(box1white, box2white): 
    m1 = combinations(7, box1white) * combinations(3, 2-box1white)
    PA1 = m1/n1
    m2 = combinations(9, box2white) * combinations(2, 2-box2white)
    PA2 = m2/n2
    return PA1*PA2
# 4a
print('4a', PA1xPA2(2, 2)) # 0.30545
# 4b
PA = 0
for i in [[2,0], [1,1], [0,2]]:
    PA += PA1xPA2(i[0], i[1])
print('4b', PA) # 0.204848
# 4c
PA = 0
for i in range(0,3):
    for j in range(0,3):
        if i!=0 or j!=0:
            PA += PA1xPA2(i, j)
print('4c', PA) # 0.99879
print('4c', 1-PA1xPA2(0, 0)) # 0.99879