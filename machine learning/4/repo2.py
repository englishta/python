import numpy as np 
from scipy.stats import t

def ryotan_t(x1, x2, alpha):
    x1_bar = np.mean(x1) # 標本平均
    x2_bar = np.mean(x2) # 標本平均
    N1 = np.size(x1) # 標本サイズ
    N2 = np.size(x2) # 標本サイズ
    s2_1 = np.var(x1, ddof=1) # 標本不偏分散
    s2_2 = np.var(x2, ddof=1) # 標本不偏分散
    s2 = ((N1-1)*s2_1 + (N2-1)*s2_2) / (N1+N2-2) # 標本不偏分散
    T = (x1_bar - x2_bar) / np.sqrt(s2/N1+s2/N2) # 検定統計量

    m = N1+N2-2 # 自由度
    Left = t.ppf(alpha/2, df=m) # 棄却域
    Right = t.ppf(1-alpha/2, df=m) # 棄却域
    p_value = t.cdf(T, df=m) # p値
    print(*[Left, Right, p_value, T])
    if p_value>0.025 and Left<T and T<Right:
        print("Saitaku:H0")
    else:
        print("Not,H0")


def relation_t(x, alpha, mu):
    x_bar = np.mean(x)      #標本平均
    s2 = np.var(x, ddof=1)  #標本不偏分散
    N = np.size(x)          #標本サイズ
    T = (x_bar-mu)/np.sqrt(s2/N)
    Left = t.ppf(alpha/2, df=N-1)
    Right = t.ppf(1-alpha/2, df=N-1)
    p_value = 1-t.cdf(T, df=N-1)
    print(*[Left, Right, p_value, T])
    if p_value>0.025 and Left<T and T<Right:
        print("Saitaku:H0")
    else:
        print("Not,H0")

#H0:差が無い、(μ1 = μ2)
#H1:差がある、(μ1 != μ2)
x1 = [12.8, 4.8, 9.3, -2.7, 9.9, 15.2, 21.4, 6.9, -4.8, -4.5, 9.1, -3.5]
x2 = [6.3, -8.5, -2.4, 4.9, -11.7, -2.7, 10.3, 14.2, 1.5, -13.6, 5.2, -4.8]
x = np.array(x1) - np.array(x2)
ryotan_t(x1, x2, 0.05)
relation_t(x, 0.05, 0)

