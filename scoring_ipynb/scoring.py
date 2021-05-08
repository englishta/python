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


# path to notebook(.ipynb)
p_nb = pathlib.Path("./answer/")

# notebooks(.ipynb)
for _nb in p_nb.glob("*.ipynb"):
    # load json (*.ipynb)
    with open(_nb, "r")as f:
        nb = json.load(f)
        cells = nb["cells"]
        
    score = 0
    #pprint(cells)
    
    # q1
    # identify cell
    _cn = identify_cell(sentence="## 問1\n",
                        cells=cells)
    ans_cell = cells[_cn + 1]
    
    try:
        result = ans_cell['outputs'][0]["text"][0]
        if result == "Hello World!\n":
            score += 1
    except:
        pass
    
    # q2
    # identify cell
    _cn = identify_cell(sentence="## 問2\n",
                        cells=cells)
    ans_cell = cells[_cn + 1]
    
    try:
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