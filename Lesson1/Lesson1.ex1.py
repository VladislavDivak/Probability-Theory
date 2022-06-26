from math import factorial

def combinations(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

def arrangements(n, k):
    return int(factorial(n)/factorial(n-k))

def permutations(n):
    return int(factorial(n))

### Excercise 1 ###
#Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.#

total_combinations = combinations(52, 4)
a_favourable = combinations(13, 4)
a_prob = a_favourable/total_combinations
print(f'Answer a: {a_prob}')

aces_1 = combinations(4, 1) * combinations(48, 3)
aces_2 = combinations(4, 2) * combinations(48, 2)
aces_3 = combinations(4, 3) * combinations(48, 1)
aces_4 = 1

b_favourable = aces_1 + aces_2 + aces_3 + aces_4
b_prob = b_favourable/total_combinations
print(f'Answer b: {b_prob}')


