from math import factorial

### Excersize 1 ###
#Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
#Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз
def combinations(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

def binominal (n, k, p):
    return combinations(n, k)*(p**k)*((1-p)**(n-k))

print(f'Answer: {binominal(100,85,0.8)*100: .3f}%')
#Answer:  4.806%
