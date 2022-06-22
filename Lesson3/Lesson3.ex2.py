from math import factorial

### Excersize 2 ###
# В первом ящике находится 8 мячей, из которых 5 - белые.
# Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4.
# Какова вероятность того, что 3 мяча белые?

def combinations(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

total_1basket = combinations(8,2)
total_2basket = combinations(12,4)
total_combo = total_1basket * total_2basket

scenario_1 = combinations(5,2)*5*combinations(7,3)
scenario_2 = 5*3*combinations(5,2)*combinations(7,2)
scenario_3 = combinations(3,2)*combinations(5,3)*7
favourable_combo = scenario_1 + scenario_2 + scenario_3

answer = favourable_combo/total_combo

print(f'Answer: {answer*100: .3f}%')
#Answer:  36.869%
