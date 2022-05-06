import itertools

'''
itertools模块的使用，常用于操作迭代对象的函数
函数的介绍
count()
cycle()
repeat()
talkwhile()
chain()
groupby()
'''

# count()会创建一个无限的迭代器
natuals = itertools.count(1)
for n in natuals:
    print(n)

# cycle()会传入一个序列无限重复下去
cs = itertools.cycle('ABC')
for c in cs:
    print(c)

# repeat()负责把一个元素无限重复下去，第二个函数可以限制重复的次数
ns = itertools.repeat('A', 8)
for n in ns:
    print(n)

# takewhile()函数根据条件来截取一个有限的序列

natuals = itertools.count(1)
# 进行截止
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

# chain()，可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'BCS'):
    print(c)

# groupby()把迭代器中相邻的重复元素跳出来进行组合

for key, sroup in itertools.groupby('AAABBBCCCDDD'):
    print(key, list(sroup))

for key, sroup in itertools.groupby('AAaaBBbb', lambda c: c.upper()):
    print(key, list(sroup))
