# 採点基準
# Q1 答えが合っている+1, print関数が使われている+1 
# Q2 答えが合っている+1, mathモジュールが使われている+1 
# 4点満点

import pathlib
import glob
import json
from pprint import pprint

N=4# 項目数
v2 = [1]*N # 部分点の点数配分
# 部分点の項目
detail = ["Q1 答えが合っている", "Q1 print関数が使われている",
    "Q2 答えが合っている", "Q2 mathモジュールが使われている"]

def identify_cell(sentence, cells, cell_type='markdown'):
    """全てのセルから条件に一致するセルの番号をreturn"""
    for i, _cell in enumerate(cells):
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
    # 部分点の項目
    p_nb = pathlib.Path("./answer/")

    for _nb in p_nb.glob("*.ipynb"):
        v1 = [0]*N # 部分点のリスト
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
            if fn1(ans_cell['source'], "print"): v1[1]+=v2[1]
            result = ans_cell['outputs'][0]["text"][0]
            if result == "Hello World!\n":
                v1[0]+=v2[0]
                
        except:
            pass
        
        # q2
        _cn = identify_cell(sentence="## 問2\n",
                            cells=cells)
        ans_cell = cells[_cn + 1]
        
        try:
            # print(*ans_cell['source']) #ソースコードを取り出す
            if fn1(ans_cell['source'], "import math"): v1[3]+=v2[3]
            result = ans_cell['outputs'][0]["text"][0]
            if result == "3628800\n":
                v1[2]+=v2[2]
        except:
            pass

        # 点数をipynbに書き込む    
        _cn = identify_cell(sentence="## 評価\n",
                            cells=cells)

        # score cellの上書き
        review = ""
        for i in range(N):
            review+=detail[i]+" : "+str(v1[i])+"点\n"
            
        cells[_cn + 1] = {'cell_type': 'code',
                            'execution_count': None,
                            'metadata': {},
                            'outputs': [],
                            'source': ["合計得点: "+str(sum(v1))+"点\n"+review]}

        # 解答用のipynbにdump (上書き)
        json.dump(nb, _nb.open("w"))


if __name__ == "__main__":
    Main()
