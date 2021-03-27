# %%

import numpy as np
x = np.array([[1,2,3], [4,5,6]])
print("x:\n{}".format(x))

# %%
from scipy import sparse
#対角成分が1でそれ以外が0の2次元numpy配列を作る

eye = np.eye(4)
print('eye:\n{}'.format(eye))

# %%
#numpy配列をSciPyのCSRの疎行列に変換する
#非ゼロ要素だけが格納される
eye[0, 2] = 5
print(eye)
sparse_matrix = sparse.csr_matrix(eye)
print('sparse_matrix:\n{}'.format(sparse_matrix))
# %%
data = np.ones(4)
row_idices = np.arange(4)
col_indices = np.arange(4)
print(data)
print(row_idices)
print(col_indices)

# %%
eye_coo = sparse.coo_matrix((data, (row_idices, col_indices)))
print(eye_coo)
# %%
#2020 11/27
from sklearn.datasets import load_iris
iris_dataset = load_iris()


# %%
print("key of iris_dataset")
print(iris_dataset.keys())
# %%
print(iris_dataset['DESCR'][:193] + "\n...")

# %%
print("Target name : {}".format(iris_dataset['target_names']))
# %%

print("Feature names: \n{}".format(iris_dataset['feature_names']))
# %%
print("Type of data\n{}".format(type(iris_dataset['data'])))

# %%
print("shape of data : \n{}".format(iris_dataset['data'].shape))
# %%
print("First five columns of data")
print(iris_dataset['data'][:5])

# %%
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = a[:2]
b

# %%
print("Type of target: {}".format(type(iris_dataset['target'])))

# %%
print("shape of target: {}".format(iris_dataset['target'].shape))

# %%
print(iris_dataset['target'])

# %%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state = 0)

# %%
print("X_train shape : {}".format(X_train.shape))
print("y_train shape : {}".format(y_train.shape))
print("X_test shape : {}".format(X_test.shape))
print("y_test shape : {}".format(y_test.shape))

# %%
import pandas as pd
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset['feature_names'])
iris_dataframe
# %%
import mglearn#色のをいい感じにしてくれもの
import pandas as pd
pd.plotting.scatter_matrix(iris_dataframe, c = y_train, marker = '.', hist_kwds={'bins':20}, s = 60, alpha = .8, figsize = (8, 8), cmap = mglearn.cm3)
#c = llll
#コラムllllによって色分けする
# %%
#k近傍法
k = 5
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=k)

knn.fit(X_train, y_train)
# %%
#予測を行う
#注意！！np.array([[]])括弧の数
X_new = np.array([[5, 2.9, 1, 0.2]])
prediction = knn.predict(X_new)
print(prediction)
print(iris_dataset['target_names'])
print(iris_dataset['target_names'][prediction])
# %%
#精度

y_pred = knn.predict(X_test)
print("Test set prediction:\n{}".format(y_pred))
# %%
print("Test set score: {:.2f}".format(np.mean(y_pred==y_test)))

# %%

print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))
# %%
