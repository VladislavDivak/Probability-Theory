from math import factorial

### Excersize 5 ###
# Устройство состоит из трех деталей.
# Для первой детали вероятность выйти из строя в первый месяц равна 0.1,
# для второй - 0.2, для третьей - 0.25.
# Какова вероятность того, что в первый месяц выйдут из строя:
# а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?

def combinations(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

def binominal (n, k, p):
    return combinations(n, k)*(p**k)*((1-p)**(n-k))

total_prob = 1/3*0.1 + 1/3*0.2 + 1/3*0.25

answer_1 = binominal(3,3,total_prob)
answer_2 = binominal(3,2,total_prob)
answer_3 = binominal(3,1,total_prob) + binominal(3,2,total_prob) + binominal(3,3,total_prob)
answer_4 = binominal(3,1,total_prob) + binominal(3,2,total_prob)

print(f'Answer 1: {answer_1*100: .3f}%\nAnswer 2: {answer_2*100: .3f}%\n'
      f'Answer 3: {answer_3*100: .3f}%\nAnswer 4: {answer_4*100: .3f}%')
#Answer 1:  0.616%
#Answer 2:  8.235%
#Answer 3:  45.533%
#Answer 4:  44.917%

