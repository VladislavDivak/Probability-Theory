### Excersize 1 ###
"""
Даны значения величины заработной платы заемщиков банка (zp)
и значения их поведенческого кредитного скоринга (ks):
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
Используя математические операции, посчитать коэффициенты линейной регрессии,
приняв за X заработную плату (то есть, zp - признак),
а за y - значения скорингового балла (то есть, ks - целевая переменная).
Произвести расчет как с использованием intercept, так и без.
"""
import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

zp = zp.reshape(len(zp),1)
ks = ks.reshape(len(ks),1)

#Without intercept
B = np.dot(np.linalg.inv(np.dot(zp.T,zp)),zp.T@ks)

#With intercept
zp1 = np.hstack([np.ones((len(zp),1)),zp])
B1 = np.dot(np.linalg.inv(np.dot(zp1.T,zp1)),zp1.T@ks)

print(f'Equation without intercept is ks = {B[0][0]:.2f} * zp\n\
Equation without intercept is ks = {B1[0][0]:.2f} + {B1[1][0]:.2f} * zp')
"""
Equation without intercept is ks = 5.89 * zp
Equation without intercept is ks = 444.18 + 2.62 * zp
"""