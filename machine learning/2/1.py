#repo21.csvのデータを読み込み相関係数とグラフを求めるプログラム
#実行方法
#python3 (name).py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
array = pd.read_csv('repo21.csv')
x = list(array['A'])
y = list(array['B'])
r = np.corrcoef(x, y)[0,1]
print(r)
plt.plot( x, y, '.' )
plt.xlabel( 'price' )
plt.ylabel( 'units' )
plt.show()
