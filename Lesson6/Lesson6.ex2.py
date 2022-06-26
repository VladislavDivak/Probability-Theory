### Excersize 2 ###
"""
Измерены значения IQ выборки студентов,
обучающихся в местных технических вузах:
131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
Известно, что в генеральной совокупности IQ распределен нормально.
Найдите доверительный интервал для математического ожидания с надежностью 0.95.
"""

from scipy import stats as st
from numpy import mean, std

list = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
M = mean(list)
alfa = 0.05
n = len(list)
std = std(list, ddof=1)

a1 = M + st.t.ppf(1-alfa/2,n)*std/(n**0.5)
a2 = M - st.t.ppf(1-alfa/2,n)*std/(n**0.5)

print(f'Reliable interval is [{a2:.3f}, {a1:.3f}]')
#Reliable interval is [110.670, 125.530]