### Excersize 1 ###
"""
Провести дисперсионный анализ для определения того,
есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов.
 Даны значения роста в трех группах случайно выбранных спортсменов:
 Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
 Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
 Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.
"""

import numpy as np
from scipy import stats

f = np.array([173, 175, 180, 178, 177, 185, 183, 182])
h = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
sh = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
f_calc = stats.f_oneway(f,h,sh)[0]

dfn = 2
dfd = (len(f)+len(h)+len(sh))-3
f_crit = stats.f.ppf(0.95, dfn, dfd)

print(f'Calculated F-value: {f_calc:.2f}\n\
Critical F-value: {f_crit:.2f}\n')

print('The difference is statistically significant') if f_calc>f_crit else print('the difference is insignificant')

"""
Calculated F-value: 5.50
Critical F-value: 3.39

The difference is statistically significant
"""