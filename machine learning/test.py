#UKgas.cvsのファイルを読み込み、グラフを出力するプログラム
#実行方法　python.exe (name).py

import pandas as pd
import matplotlib.pyplot as plt
x = [7.7, 8.0, 8.3, 8.1, 8.1, 8.2]
y = [245.5, 253.5, 261.8, 269.9, 278, 286.2]
plt.plot(y, x, '.-' )
plt.show()