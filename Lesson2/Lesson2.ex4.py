from math import factorial

### Excersize 4 ###
# В первом ящике находится 10 мячей, из которых 7 - белые.
# Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча.
# Какова вероятность того, что все мячи белые?
# Какова вероятность того, что ровно два мяча белые?
# Какова вероятность того, что хотя бы один мяч белый?

def combinations(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

#Scenario 1: all balls are white
total_comb_basket_1 = combinations(10,2)
favourable_basket_1 = combinations(7,2)

total_comb_basket_2 = combinations(11,2)
favourable_basket_2 = combinations(9,2)
answer_1 = (favourable_basket_1*favourable_basket_2)/(total_comb_basket_1*total_comb_basket_2)

#Scenario 2: 2 balls are white

fav_basket_1_only = combinations(7,2)
fav_basket_2_only = combinations(9,2)*combinations(3,2)
fav_mixed = 7*3*9*2

answer_2 = (fav_mixed+fav_basket_2_only+fav_basket_1_only)/(total_comb_basket_1*total_comb_basket_2)

#Scenario 3: at least 1 ball is white
fav_all_non_white = combinations(3,2)*1
answer_3 = 1-(fav_all_non_white/(total_comb_basket_1*total_comb_basket_2))

print(f'Answer 1: {answer_1*100: .3f}%\nAnswer 2: {answer_2*100: .3f}%\nAnswer 3: {answer_3*100: .3f}%')
#Answer 1:  30.545%
#Answer 2:  20.485%
#Answer 3:  99.879%
