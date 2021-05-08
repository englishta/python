# 採点基準
# Q1 答えが合っている+1, print関数が使われている+1 
# Q2 答えが合っている+1, mathモジュールが使われている+1 
# 4点満点

import pathlib
import glob
import json
from pprint import pprint

def identify_cell(sentence, cells, cell_type='markdown'):
    """全てのセルから条件に一致するセルの番号をreturn"""
    for i,_cell in enumerate(cells):
        if _cell['cell_type'] == cell_type \
           and _cell['source'][0] == sentence:
            _cell_num = i
            break
    return _cell_num

def fn1(List, code): # (文字列のリスト, 文字列)
    for x in List:
        # if x == "import math\n":
        # if x == code+'\n':
        if x.count('#'): continue
        if x.count(code):
            print("Exist "+'['+code+']', "score+=1")
            return True
    return False

def Main():
    p_nb = pathlib.Path("./answer/")

    # notebooks(.ipynb)
    for _nb in p_nb.glob("*.ipynb"):
        score = 0 # 小テストの得点
        # load json (*.ipynb)
        with open(_nb, "r")as f:
            nb = json.load(f)
            cells = nb["cells"]

        
        # q1
        # identify cell
        _cn = identify_cell(sentence="## 問1\n",
                            cells=cells)
        ans_cell = cells[_cn + 1]
        
        try:
            # print(*ans_cell['source']) #ソースコードを取り出す
            if fn1(ans_cell['source'], "print"): score+=1
            result = ans_cell['outputs'][0]["text"][0]
            if result == "Hello World!\n":
                score += 1
        except:
            pass
        
        # q2
        _cn = identify_cell(sentence="## 問2\n",
                            cells=cells)
        ans_cell = cells[_cn + 1]
        
        try:
            # print(*ans_cell['source']) #ソースコードを取り出す
            if fn1(ans_cell['source'], "factorial(10)"): score+=1
            result = ans_cell['outputs'][0]["text"][0]
            if result == "3628800\n":
                score += 1
        except:
            pass

        # 点数をipynbに書き込む    
        _cn = identify_cell(sentence="## 評価\n",
                            cells=cells)

        # score cellの上書き
        cells[_cn + 1] = {'cell_type': 'code',
                            'execution_count': None,
                            'metadata': {},
                            'outputs': [],
                            'source': ["採点結果: "+str(score)+"点"]}

        # 解答用のipynbにdump (上書き)
        json.dump(nb, _nb.open("w"))


if __name__ == "__main__":
    Main()