from math import factorial

def combinations(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

def arrangements(n, k):
    return int(factorial(n)/factorial(n-k))

def permutations(n):
    return int(factorial(n))

### Excercise 3 ###
#В ящике имеется 15 деталей, из которых 9 окрашены.
# Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все извлеченные детали окрашены?

total_combinations = combinations(15, 3)
favourable = combinations(9,3)
prob = favourable/total_combinations
print(f'Answer: {prob}')