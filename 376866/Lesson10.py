from scipy import stats


# Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов. 
# Даны значения роста в трех группах случайно выбранных спортсменов: 
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182. 
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180. 
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170. 

f = [173, 175, 180, 178, 177, 185, 183, 182]
h = [177, 179, 180, 188, 177, 172, 171, 184, 180]
w = [172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170]

# H0 mu0=mu1=mu2
# H1 mu0!=mu1 & mu0!=mu2 & mu1!=mu2

alpha = 0.05
serie = [f, h, w]

Norm_reject = sum([1 if stats.shapiro(x)[1] < alpha else 0 for x in serie]) == len(serie)
print('Нормальность reject', Norm_reject) # Нормальность reject False

print('Однородность reject', stats.bartlett(f, h, w)[1] < alpha) # Однородность reject False

print('H0 reject', stats.f_oneway(f, h, w)[1] < alpha) # H0 reject True
# есть различия среднего роста
