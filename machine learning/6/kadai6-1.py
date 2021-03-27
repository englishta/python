import numpy as np

#標準化をする関数
def standard(array):
    return (array-np.mean(array))/np.std(array, ddof=1)

#相関係数を求める関数
def soukan(array1, array2):
    array1_h = standard(array1)
    array2_h = standard(array2)
    return np.corrcoef(standard(array1_h), standard(array2_h))[0, 1]

x1 = [8, 7, 5, 4, 6, 2, 3, 9]
x2 = [8, 7, 9, 3, 8, 3, 6, 7]
x3 = [4, 7, 8, 3, 8, 5, 6, 9]
y = [18, 12, 14, 6, 12, 8, 10, 16]

indire_31y= soukan(x3, x1)*0.4997682
indire_32y= soukan(x3, x2)*0.5970736
alleff = indire_32y+indire_31y-0.1457974 

#print("3->1", soukan(x3, x1))
#print("3->2", soukan(x3, x2))
#print(alleff)
x1_h = standard(x1)
x2_h = standard(x2)
x3_h = standard(x3)
y_h = standard(y)
N = len(y)
X_h = np.c_[np.ones(N), x1_h, x2_h, x3_h] 
#ライブラリーのインポート
import statsmodels.api as sm
#モデルの設定 (最小2乗法による回帰分析)
# Ordinary Least Squares regression
model = sm.OLS(y_h, X_h)
#回帰分析の実行
results = model.fit()

#結果の詳細を表示
print( results.summary() )