# %%
import pandas as pd

obj = pd.Series([4, 7, -5, 3])
obj.values
obj.index
print(obj)


# %%
obj2 = pd.Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
obj2


# %%

obj2['a']
obj2['c']
# %%

obj2*2
# %%
print(obj)#objの値は変更されない
# %%
obj22 = obj2*2
print(obj22)




# %%
#dictonaryをSeriesに入れる,Keyがインデックス,valueがオブジェクト

sdata={'Ohio':35000, 'Texas':71000, 'Oregon':16000, 'Utah':5000} 
obj3 = pd.Series(sdata)

obj3
# %%
#keyを並べ替えて指定すると、Seriesのオブジェクトも並べ替えられる
states = ['Texas', 'Utah','Ohio','Oregon']
obj4 = pd.Series(sdata, index=states)
obj4


# %%
#Californiaインデックスのオブジェクトは存在しない
states = ['California','Utah', 'Ohio','Oregon']
obj4 = pd.Series(sdata, index=states)
obj4

# %%
pd.isnull(obj4)
# %%
pd.notnull(obj4)

# %%
obj4.isnull()
# %%
obj4.notnull()
# %%
#gattai
#両方のインデックスに存在するものだけ足し合わされる
print("----------obj3--------")
print(obj3)
print("---------obj4--------")
print(obj4)
print("--------obj3+obj4--------")
obj3+obj4


# %%
#name
obj4.name = 'population'
obj4.index.name = 'state'

obj4
# %%

obj = pd.Series([4, 7, -5, 3])
obj.values
obj.index
print(obj)

obj.index = ['a', 'b', 'c', 'd']
print(obj)


# %%
#DataFrame
#配列をvalueにもつ辞書から初期化する方法

data = {'state' : ['Ohio', 'OHIO', 'Nevada', 'Nevada'], 
'year' : [2000, 2001, 2001, 2003], 'pop' : [1.5, 1.7, 3.6, 2.4]}

frame = pd.DataFrame(data)
frame

# %%
#列の順を指定する
frame = pd.DataFrame(data, columns=['year', 'state', 'pop'])
frame

# %%
#存在しない列を指定するとNaNが代入される
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'NAN'])
frame2

# %%
#データフレームからシリーズを取り出す
#列を取り出す
#sannsyou
frame2['year']

# %%
#zokusei
frame2.year
# %%
#行をSeriesで取り出す
#indexで指定する
print(frame2)
frame2.loc[0]

# %%
#NAN列の値をスカラー値で書き変える
print(frame2)
frame2['NAN'] = 16.5
print(frame2)


# %%
#NAN列の値を配列で書き換え
print(frame2)
seq1 = [1.2, 2.4, 5.2, 3.2]
frame2['NAN'] = seq1

print()
print(frame2)

# %%
#NAN列の値をSeriesで書き換え
print(frame2)
print()

val = pd.Series([0.0, 2.22, 5.2, 3.2])
frame2['NAN'] = val
print(frame2)

# %%
#列の削除
del frame2['NAN']
print(frame2)


# %%
#state列が'Nevada'であるかどうかを示す真偽値をもった列を追加

frame2['eastern'] = frame2.state == 'Nevada'
print(frame2)

# %%
seq2 = frame2['eastern']
print(seq2)
frame2['eastern'][2] = True
print(seq2)


# %%

print(frame2)
frame2['eastern'] = frame2['state'] == 'Nevada'
print(frame2)



# %%
#列と行を入れ替えたものを表示
frame2.T
# %%
frame2
# %%

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)

# %%
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3

# %%
obj3.reindex(range(6), method='ffill')

# %%
data = {'state' : ['Ohio', 'OHIO', 'Nevada', 'Nevada'], 
'year' : [2000, 2001, 2001, 2003], 'pop' : [1.5, 1.7, 3.6, 2.4]}

frame = pd.DataFrame(data)
print(frame)
# %%
#データフレームのreindex,
#データ抽出
frame2 = frame.reindex([0, 2, 3])
print(frame2)

frame2 = frame.reindex(columns=['year', 'pop'])
print(frame2)

frame2 = frame.loc[[0, 1, 2], ['year', 'pop']]
print(frame2)
# %%
#csv読み込み
frame = pd.read_table('sample.csv')
print(frame)

new_frame = frame.reindex(columns=['ID', 'gender', 'DM', 'age'])
new_frame['young'] = new_frame['age'] <= 30 
new_frame['age+DM'] = new_frame['age'] + new_frame['DM']
new_frame = new_frame.drop('gender', axis=1)
#new_frame = new_frame.drop(0, axis=0)

print(new_frame)


# %%
#csvファイルに書き込む
new_frame.to_csv('new_data.csv')

# %%
import numpy as np
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])

obj
# %%
new_obj = obj.drop(['c', 'a'])


# %%
new_obj

# %%
df = pd.DataFrame({'A' : [0, 1, 2, 3], 'B' : [2, 3, 4, 5]})
lf = pd.DataFrame({'C' : [0, 1, 4, 5], 'D' : [4, 3, 4, 3]})

print(df)
print(lf)

# %%
#一番シンプルなデータフレームの合体
new_df = df.join(lf)
new_df

# %%
import pandas as pd
frame1 = pd.read_table('sample.csv')
print(frame1)

frame2 = frame1.drop(columns = ['ID', 'gender', 'age'])
frame3 = frame1.drop(columns = ['freq', 'DM'])

print(frame2)
print(frame3)

pd.concat([frame3, frame2])
# %%
import pandas as pd
frame = pd.read_table('sample.csv')
print(frame)
pd.get_dummies(frame['age'])


# %%
#get_dummiesの練習
import pandas as pd
import numpy as np

df = pd.DataFrame({'key':['b', 'b', 'a', 'c', 'a', 'b'], 'data1': np.arange(6)})
pd.get_dummies(df['key'])


# %%
dumy = pd.get_dummies(df['key'], prefix='key')
dumy

df[['key']].join(dumy)

# %%

df_with_dumy = df[['key', 'data1']].join(dumy)
df_with_dumy
df[['key', 'data1']]





# %%
#pd.concat([df1, df2, ...dfn], axis = 1)
#で横方向にデータフレームを連結できる
import pandas as pd

df = pd.read_table('sample.csv')

df1 = df.drop(columns = ['ID', 'gender'])
df2 = df.drop(columns = ['age', 'freq', 'DM'])

pd.concat([df1, df2], axis = 1)


# %%
#df[DM] が1かつ年齢が30未満の人を抽出したデータフレーム
df[(df['DM'] == 1) & (df['age'] < 30)]

# %%
