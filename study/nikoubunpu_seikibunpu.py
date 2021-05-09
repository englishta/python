#%%
import math
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(1, 1, 10000)
plt.hist(x)
plt.grid(True)
# %%
# 正規分布
from scipy.stats import norm
n = 10000
p = 0.4 # 確率
h = n*p #平均
b = n*p*(1-p)
scale = b**0.5 # 標準偏差
# N(np, np(1-p)) N(平均, 分散)

start = int(h-scale*5)
end = int(h+scale*5)
x = np.arange(start, end, 1)
y = norm.pdf(x, loc=h, scale = scale)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.grid(color = 'gray')
ax.plot(x, y, color = 'blue')
plt.show()

# %%
# 二項分布
from scipy.stats import binom
n = 10000 # 試行回数
p = 0.4 # 確率
h = n*p #平均
b = n*p*(1-p) # 分散
scale = b**0.5 # 標準偏差
start = int(h-scale*5)
end = int(h+scale*5)
x = np.arange(start, end, 1)
y = binom.pmf(x, n, p)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.grid(color = 'gray')
ax.plot(x, y, color = 'blue')
plt.show()
# %%

