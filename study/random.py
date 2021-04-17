import numpy as np
data = np.random.rand(10)
# print(data)

# サイコロがとりうる値を配列に格納
dice_data = np.array([1, 2, 3, 4, 5, 6])
# サイコロを1000回振る
calc_steps = 1000
# 1〜6のデータの中から、1000回の抽出を実施
dice_rolls = np.random.choice(dice_data, calc_steps)
# それぞれの数字がどれくらいの割合で抽出されたか計算
for i in range(1, 7):
    pi = len(dice_rolls[dice_rolls==i]) / calc_steps
    print(i, ":", pi)
