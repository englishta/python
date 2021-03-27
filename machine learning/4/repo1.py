#判定関数
#H0:µ=350（帰無仮説)
#H1:µ!=350 (対立仮説)
#両端検定

def interval_t(alpha, x, mu):
    import numpy as np
    from scipy.stats import t
    x_bar = np.mean(x)      #標本平均
    s2 = np.var(x, ddof=1)  #標本不偏分散
    N = np.size(x)          #標本サイズ
    T = (x_bar-mu)/np.sqrt(s2/N)
    Right = t.ppf(1-alpha/2, df=N-1)
    Left = t.ppf(alpha/2, df=N-1)
    p_value = 1-t.cdf(T, df=N-1)
    print('Left=', Left,'Right=', Right)
    print('p_value=', p_value, 't=', T)
    if Left<T and T<Right and p_value>alpha/2:
        print('Saitaku')
    else: print('Kikyaku')

x = [361, 355, 349, 358, 352, 364]
interval_t(0.05, x, 350)

