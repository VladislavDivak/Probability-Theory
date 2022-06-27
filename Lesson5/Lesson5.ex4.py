
###Excersize 4###
"""
Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья составляет 200 г.
Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
Известно, что их веса распределены нормально.
Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%?
(Провести двусторонний тест.)
"""

from scipy import stats as st
from numpy import mean, std

m_init = 200
sample = [202, 203, 199, 197, 195, 201, 200, 204, 194, 190]
M = mean(sample)
alfa = 0.01
n = len(sample)
std = std(sample, ddof=1)

t_score = abs(M-m_init)/(std/n**0.5)
t_score_alfa = st.t.ppf(1-alfa,n)

print(f'H_0 is correct, with 95% confidence level the general mean is 200g') if t_score <= t_score_alfa \
        else print(f'H_1 is correct, with 95% confidence level the general mean is not 200g')

