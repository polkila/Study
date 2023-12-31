from math import sqrt
from scipy import stats
import numpy as np


# Задача 1. Когда используется критерий Стьюдента, а когда Z –критерий?

# Z –критерий используется, когда известна сигма генеральной совокупности.
# Критерий Стьюдента используется, когда сигма генеральной совокупности не известна.



# Задачи 2,3 решать вручную
# Задача 2. Проведите тест гипотезы. Утверждается, что шарики для подшипников, изготовленные
# автоматическим станком, имеют средний диаметр 17 мм.
# Используя односторонний критерий с α=0,05, проверить эту гипотезу, если в выборке из
# n=100 шариков средний диаметр
# оказался равным 17.5 мм, а дисперсия генеральной совокупности известна и равна 4 кв. мм.
M = 17
# H0 M=17
alpha = 0.05
n = 100
# H1 = M>17
X = 17.5
Dx = 4
sigma = sqrt(Dx)
Zn = (X-M)/(sigma/sqrt(n))
print('Zn', Zn) # Zn 2.5
# ПКО (t(1-alpha),∞)
# t1 = 1.654

# t1 = stats.norm.ppf(1-alpha)
# print('t1', t1) # t1 1.6448536269514722

# abs(Zn) > t1 
# H0 отвергается
# средний диаметр > 17 мм



# Задача 3. Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья
# составляет 200 г.
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
# 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
# Известно, что их веса распределены нормально.
# Верно ли утверждение продавца, если учитывать, что уровень значимости 1%? (Провести двусторонний тест.)

M = 200
weights = [202, 203, 199, 197, 195, 201, 200, 204, 194, 190]
alpha = 0.01
# H0 M=200
# H1 M!=200
n = len(weights)
X = sum(weights)/n
print('X', X) # X 198.5
Dx = sum([pow(x-M, 2) for x in weights])/(n-1)
print('Dx', Dx) # Dx 22.333333333333332
# Dx = np.array(weights).var(ddof=1)
# print('Dx', Dx) # Dx 19.833333333333332
sigma = sqrt(Dx)
print('sigma', sigma) # sigma 4.725815626252608
# sigma = np.std(np.array(weights), ddof=1)
# print(sigma) # 4.453463071962462
tn = (X-M)/(sigma/sqrt(n))
print('tn', tn) # tn -1.0037244076773089
p = 1 - alpha/2 # 0.995
# t = 3.25
# ДКО (-∞, t(alpha/2)) U (t(1-alpha/2), ∞)   
# (-∞, -3.25) U (3.25, ∞)

# t1 = stats.t.ppf(alpha/2, n-1)
# print('t1', t1) # t1 -3.24983554401537
# t2 = stats.t.ppf(1-alpha/2, n-1) 
# print('t2', t2) # t2 3.24983554401537

# t1 < abs(tn), abs(tn) < t2
# H0 не отвергается
# средний вес пачки печенья составляет 200 г



# Задачу 4 решать с помощью функции.
# Задача 4. Есть ли статистически значимые различия в среднем росте матерей и
# дочерей?
# Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169, 165
# Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160, 163

heights1 = np.array([172, 177, 158, 170, 178,175, 164, 160, 169, 165])
heights2 = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160, 163])
print('result', stats.ttest_ind(heights1, heights2)) # statistic=0.4138411497680053, pvalue=0.68387966499013, df=18.0
# H0 различий нет
# H1 различия есть
# alpha = 0.1
# pvalue > alpha
# H0 не отвергается на уровне значимости alpha = 0.1


