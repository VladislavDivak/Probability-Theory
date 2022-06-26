from math import factorial

def combinations(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

def arrangements(n, k):
    return int(factorial(n)/factorial(n-k))

def permutations(n):
    return int(factorial(n))

### Excercise 2 ###
#На входной двери подъезда установлен кодовый замок,
# содержащий десять кнопок с цифрами от 0 до 9.
# Код содержит три цифры, которые нужно нажать одновременно.
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

total_combinations = combinations(10, 3)
prob = 1/total_combinations
print(f'Answer: {prob}')