from math import factorial

def combinations(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

def arrangements(n, k):
    return int(factorial(n)/factorial(n-k))

def permutations(n):
    return int(factorial(n))

### Excercise 4 ###
#В лотерее 100 билетов. Из них 2 выигрышных.
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

total_combinations = combinations(100, 2)
prob = 1/total_combinations
print(f'Answer: {prob}')