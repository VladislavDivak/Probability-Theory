### Excersize 1 ###
"""
Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy
Полученные значения должны быть равны.
Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,
а затем с использованием функций из библиотек numpy и pandas.
"""
import numpy as np
import pandas as pd

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

cov_manual = np.mean(zp*ks) - np.mean(zp)*np.mean(ks)
cov_np = np.cov(zp,ks,ddof=0)

std_zp = np.std(zp)
std_ks = np.std(ks)

pearson_manual = cov_manual/(std_zp*std_ks)
peason_numpy = np.corrcoef(zp,ks)

zp_pd = pd.Series([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks_pd = pd.Series([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
pearson_pandas = zp_pd.corr(ks_pd)

print(f'Covariance manual = {cov_manual}\n\
Covariance numpy = {cov_np[1][0]} (shifted correlation)\n\
Pearson manual = {pearson_manual}\n\
Pearson numpy = {peason_numpy[1][0]}\n\
Pearson pandas = {pearson_pandas}')

"""
Covariance manual = 9157.839999999997
Covariance numpy = 9157.84 (shifted correlation)
Pearson manual = 0.8874900920739158
Pearson numpy = 0.8874900920739162
Pearson pandas = 0.8874900920739162
"""
