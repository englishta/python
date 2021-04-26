#%%
import numpy as np
data = np.array([9, 2, 3, 4, 10, 6, 7, 8, 1, 5])
data


# %%
data.dtype
# %%
print('次元数', data.ndim)
print('要素数', data.size)
# %%
data*2
# %%
print('掛け算', np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])*np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print('累乗', np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])**2)
print('割り算', np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])/np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

# %%
print('そのまま', data)
data.sort()
print('ソート後', data)
# %%
data = np.array([9, 2, 3, 4, 10, 6, 7, 8, 1, 5])
print(sorted(data))
print(data)
data.sort()

# %%
# numpy配列の降順ソート
data[::-1].sort()
data

# %%
print(data.min()) #最小値
print(data.max()) #最大値
print(data.sum()) #総和
print(data.cumsum()) #累積和の配列
print(data.cumsum()/data.sum()) #積み上げ割合

# %%
# 乱数
import numpy.random as random
random.seed(0)
rnd_data = random.randn(10)
rnd_data
# %%
data = np.array([9, 2, 3, 4, 10, 6, 7, 8, 1, 5])
# 抽出対象データ

# 10個を抽出(重複あり, 復元抽出)
print(random.choice(data, 10))

# %%
#　10個を抽出(重複なし、非復元抽出)
print(random.choice(data, 10, replace=False))

# %%
np.arange(9)
#%%
array1 = np.arange(9).reshape(3, 3)
array1


# %%
# array[行範囲, 列範囲]
# 1行目抜き出し
print(array1[0, :])

print(array1[0:2, :])
print(array1[:, 1:3])
print(array1[0:2, 1:3])
# %%
array2 = np.arange(9, 18).reshape(3, 3)
print(array2)
# %%
print(array1)
print(np.dot(array1, array2)) #行列の積
print(array1*array2) #行列の要素ごとの掛け算
print(array1+array2) #行列の足し算
# %%
# 要素が0や1の行列を作る
print(np.zeros((2, 3), dtype = np.int64))
print(np.ones((2, 3),  dtype = np.float64))


# %%
# 固有値と固有ベクトルを求める

import numpy as np
A = np.array([[2, 4], [0, 4]])
koyuti, koyuvec = np.linalg.eig(A)
print(koyuti)
print(koyuvec)
# %%

