#判定関数
#H0:交代後もばらつき具合に変化なし（帰無仮説）を立てる
#Chi_2関数の戻り値：True=帰無仮説が妥当だ、False=帰無仮説を棄却
def Chi_2(alpha, x, bunsan):
    import numpy as np
    from scipy.stats import chi2
    s2 = np.var(x, ddof=1)  #標本不偏分散
    N = np.size(x)          #標本サイズ
    Chi2 = (N-1)*s2/bunsan**2
    Left=chi2.ppf(alpha, df=N-1)
    p_value=chi2.cdf(Chi2, df=N-1)
    print('Left', Left)
    print('p_value=', p_value)
    if p_value<alpha: print('H0 is wrong=kikyaku')
    else: print('H0 is OK=saitaku')

x = [35.2, 34.5, 34.9, 35.2, 34.8, 35.1, 34.9, 35.2, 34.9, 34.8]
Chi_2(0.05, x, 0.4)