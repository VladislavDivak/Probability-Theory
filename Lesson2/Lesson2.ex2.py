from math import factorial
import numpy as np
### Excersize 2 ###
# Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
# Какова вероятность, что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?

def puasson (n, p, m):
    return ((n*p)**m / factorial(m)) * np.exp(-(n*p))

answer_1 = puasson(5000,0.0004,0)
answer_2 = puasson(5000,0.0004,2)

print(f'Answer 1: {answer_1*100: .3f}%\nAnswer 2: {answer_2*100: .3f}%')
#Answer 1:  13.534%
#Answer 2:  27.067%