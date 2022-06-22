
###Excersize 3###
"""
Проведтите тест гипотезы. Утверждается, что шарики для подшипников,
изготовленные автоматическим станком, имеют средний диаметр 17 мм.
Используя односторонний критерий с α=0,05, проверить эту гипотезу,
если в выборке из n=100 шариков средний диаметр оказался равным 17.5 мм,
а дисперсия известна и равна 4 кв. мм.
"""

from scipy import stats as st

m_init = 17
M = 17.5
alfa = 0.05
n = 100
std = 2

z_score = (M-m_init)/(std/n**0.5)
z_score_alfa = st.norm.ppf(1-alfa)

print(f'H_0 is correct, with 95% confidence level the general mean is 17mm') if z_score <= z_score_alfa \
        else print(f'H_1 is correct, with 95% confidence level the general mean is not 17mm')

