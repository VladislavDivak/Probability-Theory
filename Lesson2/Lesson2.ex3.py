from math import factorial

### Excersize 3 ###
#Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

def combinations(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

def binominal (n, k, p):
    return combinations(n, k)*(p**k)*((1-p)**(n-k))

print(f'Answer: {binominal(144,70,0.5)*100: .3f}%')
#Answer:  6.281%
