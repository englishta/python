# %%
import pandas as pd
import numpy as np
import graphviz
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from IPython.display import Image

data = pd.DataFrame({
        "buy(y)":[True,True,True,True,True,True,True,False,False,False,False,False,False],
        "high":[4, 5, 3, 1, 6, 3, 4, 1, 2, 1, 1,1,3],
        "size":[30, 45, 32, 20, 35, 40, 38, 20, 18, 20, 22,24,25],
        "autolock":[1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0,1,0]
    })

y = data.loc[:,["buy(y)"]]
X = data.loc[:,["high", "size","autolock"]]


clf = DecisionTreeClassifier()
clf.fit(X, y)
print(clf.classes_)

dot_data = export_graphviz(
    clf,
    class_names=["False", "True"],
    out_file=None,
    filled=True,
    rounded=True,
)

graph = graphviz.Source(dot_data)
graph.render("room_data", format="png")


z = pd.DataFrame({
        "high":[2, 3, 1],
        "size":[25, 18, 22],
        "autolock":[1, 0, 1]
    })
z2 = z[["high", "size","autolock"]].values

y_est = clf.predict(z2)
print(y_est)

#一番最後に記述する
graph
# %%
