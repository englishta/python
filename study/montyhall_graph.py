import random
import matplotlib.pyplot as plt
import numpy as np


def Main():
    print("Monty Hall Simulation Start!!")
    cnt = 10000 # ゲームの試行回数
    # 扉を変更しないゲームを実施
    win_cnt1, v1 = game("Nochange", cnt)
    print("Nochange game : ", win_cnt1, "/", cnt)
    # 扉を変更するゲームを実施
    win_cnt2, v2 = game("change", cnt)
    print("  change game : ", win_cnt2, "/", cnt)

    yes_array = [0]
    no_array = [0]
    for i in range(1, len(v1)):
        yes_array.append(v1[i]/i)
    for i in range(1, len(v2)):
        no_array.append(v2[i]/i)
        
    plt.plot(yes_array)
    plt.plot(no_array)
    plt.show()


def game(Mode, Gcount):
    Wincnt_No=0
    array_No = [0]
    if Mode == "Nochange":
        for i in range(Gcount):
            Wincnt_No+=Dogame_nochange()
            array_No.append(Wincnt_No)
        return Wincnt_No, array_No

    Wincnt_Yes = 0
    array_Yes = [0]
    if Mode == "change":
        for i in range(Gcount):
            Wincnt_Yes+=Dogame_change()
            array_Yes.append(Wincnt_Yes)
        return Wincnt_Yes, array_Yes

def Dogame_nochange():
    # 宝の場所をランダムに選ぶ
    treasure = random.randint(1, 3)
    # プレイヤの最初の扉を選ぶ
    firstChoise = random.randint(1, 3)
    if firstChoise == treasure: return 1
    else: return 0

def Dogame_change():
    # 宝の場所をランダムに選ぶ
    treasure = random.randint(1, 3)
    # プレイヤの最初の扉を選ぶ
    firstChoise = random.randint(1, 3)
    # montyChoiseがtreasureとfirstChoise以外のものである必要がある
    while(1):
        montyChoise = random.randint(1, 3)
        if(montyChoise!=treasure and montyChoise!=firstChoise): break

    # montyChoise, firstChoise以外の扉に変える1
    while(1):
        secondChoise = random.randint(1, 3)
        if(secondChoise!=montyChoise and secondChoise!=firstChoise): break
        
    if secondChoise == treasure: return 1
    else: return 0


if __name__ == "__main__":
  Main()

