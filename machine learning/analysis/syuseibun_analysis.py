# %%
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

x1 = [86, 71, 42, 62, 96, 39, 50, 78, 51, 89] 
x2 = [79, 75, 43, 58, 97, 33, 53, 66, 44, 92]
x3 = [67, 78, 39, 98, 61, 45, 64, 52, 76, 93]
x4 = [68, 84, 44, 95, 63, 50, 72, 47, 72, 91]


x1h = (x1-np.mean(x1))/np.std(x1, ddof=1)
x2h = (x2-np.mean(x2))/np.std(x2, ddof=1)
x3h = (x3-np.mean(x3))/np.std(x3, ddof=1)
x4h = (x4-np.mean(x4))/np.std(x4, ddof=1)

COV = np.cov([x1h, x2h, x3h, x4h])
L, A = np.linalg.eig(COV)
rate = L/np.sum(L)#寄与率を求める配列
#データフレームへ変換
df_rate = pd.DataFrame(data = rate, 
                      columns = ['寄与率'],
                      index = ["主成分{}".format(x+1) for x in range(4)])

z1 = A[0,0] * (x1h-np.mean(x1h)) + A[1,0] * (x2h-np.mean(x2h)) + A[2,0] * (x3h-np.mean(x3h)) + A[3,0] * (x4h-np.mean(x4h))
z2 = A[0,1] * (x1h-np.mean(x1h)) + A[1,1] * (x2h-np.mean(x2h)) + A[2,1] * (x3h-np.mean(x3h)) + A[3,1] * (x4h-np.mean(x4h))


frame = pd.DataFrame({'X1' : x1, 'X2' : x2, 'x3' : x3, 'x4' : x4, 'x1h':x1h, 'x2h':x2h, 'x3h':x3h, 'x4h':x4h, 'z1':z1, 'z2':z2})
frame = frame.assign(z1_order=len(frame.z1) - stats.mstats.rankdata(frame.z1)+1)
print("L=", L)
print("A=", A)
print(df_rate)
plt.plot(z1, z2, '.', color = 'red')

# %%
frame
# %%
# 寄与率を累積する
ruiseki = np.cumsum(rate)

# 0を連結
ruiseki = np.hstack([0, ruiseki])
ruiseki
# グラフを描画
plt.plot(ruiseki, "-o", color = 'deeppink')
plt.xlabel("Principal component")
plt.ylabel("Cumulative contribution rate")
# %%
frame2 = pd.DataFrame({'Japanese' : x1h, 'English' : x2h, 'Math' : x3h, 'Seience' : x4h})
frame2
# %%
pd.plotting.scatter_matrix(frame2, alpha=0.5, figsize=(8, 8), color = 'red')

# %%
import sklearn
from sklearn.decomposition import PCA

frame3 = pd.DataFrame({'Japanese' : x1, 'English' : x2, 'Math' : x3, 'Science' : x4})
pca = PCA()
pca.fit(frame3)
value = pca.transform(frame3)
value
# %%
frame4 = pd.DataFrame(data = value, columns = ["主成分{}".format(x+1) for x in range(len(frame3.columns))])
frame4

# %%
# モデルpcaの寄与率を算出
ev_ratio = pca.explained_variance_ratio_
ev_ratio

# %%
df_evr = pd.DataFrame(data = ev_ratio, 
                      columns = ['寄与率'],
                      index = ["主成分{}".format(x+1) for x in range(len(frame3.columns))])
df_evr

# %%
# 寄与率を累積する
cc_ratio = np.cumsum(ev_ratio)

# 0を連結
cc_ratio = np.hstack([0, cc_ratio])

# グラフを描画
plt.plot(cc_ratio, "-o")
plt.xlabel("syuseibun")
plt.ylabel("ruiseki_kiyoritu")

# %%
