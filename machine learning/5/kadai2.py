import matplotlib.pyplot as plt
import numpy as np


def jukaiki_bunseki(x1, x2, x3, y):

    N = np.size(x1) # 標本数
    Y = np.c_[y]
    X = np.c_[x1, x2, x3, np.ones(N)]

    tmp = np.dot(X.T, X) # XTX
    r1 = np.linalg.inv(tmp) # (XTX)^-1 逆行列
    r2 = np.dot(X.T, Y) # XTY
    A = np.dot(r1, r2) # 係数ベクトル

    a1 = A[0] # 傾き
    a2 = A[1] # 傾き
    a3 = A[2] # 傾き
    b = A[3] # 切片b


    # [追加機能]回帰直線の妥当性を評価する
    Y_hat = a1*x1 + a2*x2 + a3*x3 + b # 予測値
    C = np.corrcoef(Y_hat, y)[0,1] # 相関係数
    # 決定係数
    R2 = np.sum( (Y_hat-np.mean(y))**2 ) / np.sum( (y-np.mean(y))**2 )

    return a1, a2, a3, b, C, R2

x1 = [8, 7, 5, 4, 6, 2, 3, 9]
x2 = [8, 7, 9, 3, 8, 3, 6, 7]
x3 = [4, 7, 8, 3, 8, 5, 6, 9]
y = [18, 12, 14, 6, 12, 8, 10, 16]

for x in jukaiki_bunseki(x1, x2, x3, y):
    print(x)
