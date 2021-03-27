# %%
#zipの使い方
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
#for x, y in zip(seq1, seq2):
#    print(x, y)

for i, (a, b) in enumerate(zip(seq1, seq2)):
    print(i, a, b)

zipped = zip(seq1, seq2)

a, b = zip(*zipped)#分解する
print(a)
print(b)

# %%
#set
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
wa = a.union(b)#a | b
seki = a.intersection(b)# a & b

print(wa)
print(seki)
# %%





