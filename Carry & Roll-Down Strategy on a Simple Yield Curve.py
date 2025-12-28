import pandas as pd
from pandas_datareader import data as pdr
import numpy as np
import matplotlib.pyplot as plt

tickers = ['GS2', 'GS5', 'GS10']
rates = pdr.DataReader(tickers, 'fred', start='2000-01-01').dropna()
rates = rates / 100  # passer en décimal
rates = rates.resample('M').last()

#print(rates)

#Prix d’un zero-coupon
# prix aujourd’hui (t) d’une obligation zéro-coupon qui arrive à maturité T

def zcb_price(y, T):
    return np.exp(-y * T)

def rolldown(y_T, y_Tm1, T):
    return -T * (y_Tm1 - y_T)

maturities = {'GS2': 2, 'GS5': 5, 'GS10': 10}

scores = pd.DataFrame(index=rates.index, columns=rates.columns)

for col, T in maturities.items():
    y_T = rates[col]
    y_Tm1 = rates[col].shift(1)  # approx T-1 mois
    rd = rolldown(y_T, y_Tm1, T)
    scores[col] = y_T + rd

#print(scores)
#Choix de la maturité optimale

best_mat = scores.idxmax(axis=1)
#print(best_mat)

#Performance mensuelle

returns = pd.DataFrame(index=rates.index, columns=rates.columns)

for col, T in maturities.items():
    dy = rates[col].diff()
    returns[col] = -T * dy + rates[col] / 12  # carry mensuel approx

#Performance de la stratégie

strategy_ret = []

for t in range(1, len(rates)):
    mat = best_mat.iloc[t-1]  # maturité choisie le mois précédent
    if pd.isna(mat):
        strategy_ret.append(0)  # pas de position si NaN
    else:
        # on utilise .loc pour aligner correctement l'index
        strategy_ret.append(returns.loc[returns.index[t], mat])

strategy_ret = pd.Series(strategy_ret, index=rates.index[1:])

#Analyse

cum = (1 + strategy_ret.fillna(0)).cumprod()

cum.plot(title='Cumulative performance: Carry & Roll-down strategy')
plt.show()

print("Sharpe:", strategy_ret.mean() / strategy_ret.std() * np.sqrt(12))
print("Vol:", strategy_ret.std() * np.sqrt(12))
print("Mean return:", strategy_ret.mean() * 12)