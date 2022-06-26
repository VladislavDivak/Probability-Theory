from scipy import stats as st

###Excersize 4###
"""
Рост взрослого населения города X имеет нормальное распределение.
Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
а). больше 182 см
б). больше 190 см
в). от 166 см до 190 см
г). от 166 см до 182 см
д). от 158 см до 190 см
е). не выше 150 см или не ниже 190 см
ё). не выше 150 см или не ниже 198 см
ж). ниже 166 см.
"""
mean = 174
std = 8
z1 = (182-mean)/std
p1 = 1 - st.norm.cdf(z1)

z2 = (190-mean)/std
p2 = 1 - st.norm.cdf(z2)

z3 = (166-mean)/std
p3 = 1 - st.norm.cdf(z3) - p2

p4 = 1 - st.norm.cdf(z3) - p1

z5 = (158-mean)/std
p5 = 1 - st.norm.cdf(z5) - p2

z6 = (150-mean)/std
p6 = st.norm.cdf(z6) + p2

z7 = (198-mean)/std
p7 = st.norm.cdf(z6) + 1 - st.norm.cdf(z7)

p8 = st.norm.cdf(z3)
print(f'а). больше 182 см = {p1*100:.2f}%\n\
б). больше 190 см = {p2*100:.2f}%\n\
в). от 166 см до 190 см = {p3*100:.2f}%\n\
г). от 166 см до 182 см = {p4*100:.2f}%\n\
д). от 158 см до 190 см = {p5*100:.2f}%\n\
е). не выше 150 см или не ниже 190 см = {p6*100:.2f}%\n\
ё). не выше 150 см или не ниже 198 см = {p7*100:.2f}%\n\
ж). ниже 166 см = {p8*100:.2f}%\n')

'''
а). больше 182 см = 15.87%
б). больше 190 см = 2.28%
в). от 166 см до 190 см = 81.86%
г). от 166 см до 182 см = 68.27%
д). от 158 см до 190 см = 95.45%
е). не выше 150 см или не ниже 190 см = 2.41%
ё). не выше 150 см или не ниже 198 см = 0.27%
ж). ниже 166 см = 15.87%
'''
