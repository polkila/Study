from math import sqrt, pi, exp
from scipy import stats

# Задача 1. Случайная непрерывная величина A имеет равномерное распределение на
# промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.
a = 200
b = 800
Mx = (a + b)/2
Dx = (b - a)**2/12
print ('Mx', Mx) # Mx 500.0
print ('Dx', Dx) # Dx 30000.0



# Задача 2. О случайной непрерывной равномерно распределенной величине B известно, что ее
# дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая
# граница равна 0.5?
# Если да, найдите ее.
Dx = 0.2
a = 0.5
b = sqrt(Dx*12) + a
print('b', b) # b 2.049193338482967



# Задача 3. Непрерывная случайная величина X распределена нормально и задана плотностью
# распределения
# f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)
# Найдите:
# а). M(X)
# б). D(X)
# в). std(X) (среднее квадратичное отклонение)
Mx = -2
Dx = 16
s = 4



# Задача 4. Рост взрослого населения города X имеет нормальное распределение, причем, средний рост равен 174 см, а среднее квадратическое отклонение равно 8 см. посчитайте, какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# 1. больше 182 см?
# 2. больше 190 см?
# 3. от 166 см до 190 см?
# 4. от 166 см до 182 см?
# 5. от 158 см до 190 см?
# 6. не выше 150 см или не ниже 190 см?
# 7. не выше 150 см или не ниже 198 см?
# 8. ниже 166 см?
# Задачу можно решить двумя способами: без использования сторонних библиотек (numpy, scipy, pandas и пр.), а затем проверить себя с помощью встроенных функций
a = 174
s = 8
def Zx(x, a, s):
    return (x-a)/s

print('1)', Zx(182, a, s), 1-.8413, 1-stats.norm.cdf(182, loc=a, scale=s)) # 1) 1.0 0.15869999999999995 0.15865525393145707
print('2)', Zx(190, a, s), 1-.9772, 1-stats.norm.cdf(190, loc=a, scale=s)) # 2) 2.0 0.022800000000000042 0.02275013194817921
print('3)', Zx(166, a, s), Zx(190, a, s), .9772-.1587, stats.norm.cdf(190, loc=a, scale=s)-stats.norm.cdf(166, loc=a, scale=s)) # 3) -1.0 2.0 0.8185 0.8185946141203637
print('4)', Zx(166, a, s), Zx(182, a, s), .8413-.1587, stats.norm.cdf(182, loc=a, scale=s)-stats.norm.cdf(166, loc=a, scale=s)) # 4) -1.0 1.0 0.6826000000000001 0.6826894921370859
print('5)', Zx(158, a, s), Zx(190, a, s), .9772-.0228, stats.norm.cdf(190, loc=a, scale=s)-stats.norm.cdf(158, loc=a, scale=s)) # 5) -2.0 2.0 0.9543999999999999 0.9544997361036416
print('6)', Zx(150, a, s), Zx(190, a, s), .00135+1-.9772, stats.norm.cdf(150, loc=a, scale=s)+1-stats.norm.cdf(190, loc=a, scale=s)) # 6) -3.0 2.0 0.024150000000000005 0.0241000299798092
print('7)', Zx(150, a, s), Zx(198, a, s), .00135+1-.99865, stats.norm.cdf(150, loc=a, scale=s)+1-stats.norm.cdf(198, loc=a, scale=s)) # 7) -3.0 3.0 0.0026999999999999247 0.002699796063260096
print('8)', Zx(166, a, s), .1587, stats.norm.cdf(166, loc=a, scale=s)) # 8) -1.0 0.1587 0.15865525393145707



# Задача 5. На сколько сигм (средних квадратичных отклонений) отклоняется рост человека,
# равный 190 см, от
# математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?
print(Zx(190, 178, sqrt(25))) # 2.4

