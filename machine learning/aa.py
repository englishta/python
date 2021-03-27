#信頼区間を計算し仮説を判定する関数
#H0:交代後も母平均に変化なし(µ=µ0)（帰無仮説)
#H1:µ>µ0 (対立仮説)
#interval_t関数の戻り値：True=帰無仮説が妥当だ、False=帰無仮説を棄却
def interval_t(alpha, x, mu):
    import numpy as np
    from scipy.stats import t
    x_bar = np.mean(x)      #標本平均
    s2 = np.var(x, ddof=1)  #標本不偏分散
    N = np.size(x)          #標本サイズ
    T = (x_bar-mu)/np.sqrt(s2/N)
    Right = t.ppf(1-alpha, df=N-1)
    p_value = 1-t.cdf(T, df=N-1)
    print('Right=', Right)
    print('p_value=', p_value, 't=', T)
    if p_value < alpha: return False
    else: return True
    
x = [44.9, 43.7, 41.2, 41.8, 41.3, 44.2]
if interval_t(0.05, x, 41.5): print("H0 is OK")
else: print('H0 is worng=kikyaku')
print(2222)
