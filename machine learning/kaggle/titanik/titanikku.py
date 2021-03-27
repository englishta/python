# %%
#タイタニック号生存者予測byketteigi
import numpy as np
import pandas as pd
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

train["is_train"] = 1
test["is_train"] = 0
data = pd.concat([train.drop(columns=["Survived"]), test])

data["Age"] = data["Age"].fillna(data["Age"].median())
data["Embarked"] = data["Embarked"].fillna("S")
data = pd.concat([data, pd.get_dummies(data["Embarked"], prefix="Embarked")], axis=1).drop(columns=["Embarked"])
data["Sex"] = pd.get_dummies(data["Sex"], drop_first=True)


feature_columns =["Pclass", "Sex", "Age", "Embarked_C", "Embarked_Q", "Embarked_S"]
feature_train = data[data["is_train"] == 1].drop(columns=["is_train"])[feature_columns]
feature_test = data[data["is_train"] == 0].drop(columns=["is_train"])[feature_columns]

target_train = train["Survived"]

#決定木の制作
from sklearn import metrics
from sklearn import tree

model = tree.DecisionTreeClassifier()
model.fit(feature_train, target_train)
pred_train = model.predict(feature_train)
metrics.accuracy_score(target_train, pred_train)

#予測する
pred_test = model.predict(feature_test)

#予測結果をcsvファイルに保存する
my_prediction = pd.DataFrame(pred_test, test["PassengerId"], columns=["Survived"])
my_prediction.to_csv("my_prediction.csv", index_label=["PassengerId"])


# %%
#決定木を描写する
import graphviz
from sklearn.tree import DecisionTreeClassifier, export_graphviz

dot_data = export_graphviz(
    model,
    class_names=["False", "True"],
    out_file=None,
    filled=True,
    rounded=True,
)

graph = graphviz.Source(dot_data)
graph.render("titanik", format="png")

graph



# %%
