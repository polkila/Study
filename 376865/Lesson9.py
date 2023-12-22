import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm


# 1. Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): 
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], 
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. 
# Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату (то есть, zp - признак), 
# а за y - значения скорингового балла (то есть, ks - целевая переменная). Произвести расчет как с использованием intercept, так и без.

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

print('Shapiro zp', stats.shapiro(zp)) # ShapiroResult(statistic=0.8886315226554871, pvalue=0.16365556418895721)
print('Shapiro ks', stats.shapiro(ks)) # ShapiroResult(statistic=0.9201253056526184, pvalue=0.35800155997276306)

n = len(zp)

# a) с использованием intercept

def get_b1(s, p, n):
    return (n*np.sum(p*s) - np.sum(s)*np.sum(p)) / (n*np.sum(s**2) - np.sum(s)**2)
    # return (np.mean(s*p) - np.mean(s)*np.mean(p)) / (np.mean(s**2) - np.mean(s)**2)

def get_a(x, y, b1):
    return np.mean(y)-b1*np.mean(x)

b1 = get_b1(zp, ks, n)
print('b1', b1) # 2.620538882402765
a = get_a(zp, ks, b1)
print('a', a) # 444.17735732435955


# Матричный способ

x = zp.reshape((-1, 1))
X = np.hstack([np.ones((n, 1)), x])
y = ks.reshape((-1, 1))
B = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T@y)
print('B', B) # [[444.17735732] [  2.62053888]]


# b) без intercept

x = zp.reshape((-1, 1))
y = ks.reshape((-1, 1))
B = np.dot(np.linalg.inv(np.dot(x.T, x)), x.T@y)
print('B', B) # [[5.88982042]]




# 2. Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept). 
# (можно использовать библиотеки питона, вместо градиентого спуска)


# a) библиотеки питона

x = zp.reshape((-1,1))
y = ks

model = LinearRegression()
regres = model.fit(x, y)
print('a', regres.intercept_) # 444.1773573243595
print('b1', regres.coef_) # [[2.62053888]]
print('R2', model.score(x, y)) # 0.7876386635293685

# без intercept

model = LinearRegression(fit_intercept=False)
regres = model.fit(x, y)
print('a', regres.intercept_) # 0
print('b1', regres.coef_) # [[5.88982042]]
print('R2', model.score(x, y)) # -0.8549037531632884

# b) градиентный спуск

x = np.array(zp)
y = np.array(ks)

def get_mse(B1, x, y, n):
    return np.sum((B1*x - y)**2) / n

alpha = 1e-6
B1 = 0.1
precise = 1e-9
B1_prev = 0

while (B1-B1_prev>precise):
    B1_prev = B1
    B1 -= alpha * (2/n) * np.sum((B1*x - y) * x)

print('B1', B1) # 5.889820385799635


# 3. (Дополнительно) Произвести вычисления как в пункте 2, но с вычислением intercept. 
# Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно 
# (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).

x = np.array(zp)
y = np.array(ks)

alpha = 1e-6
B1 = 0.1
precise = 1e-9
B1_prev = 0

while (abs(B1_prev-B1) > precise):
    B1_prev = B1
    B1 -= alpha * (2/n) * np.sum((B1*x - y) * x)
    a = get_a(x, y, B1_prev)


print('B1', B1) # 5.889820385799635
print('a', a) # 112.6722129785577


