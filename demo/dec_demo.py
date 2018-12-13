#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 作者： RandyZhang
# 时间： 2017/8/23

# 字典定义，key必须为不可变对象
dict1 = {1: 'a', 2: 'b', 3: 'c'}
print(dict1)
dict2 = {'a': 1, 2: 'b', (1, 2, 3): [4, 5, 6]}
print(dict2)

# 修改字典的值
dict1[1] = 'abcd'
print(dict1)
dict2[(1, 2, 3)].append(7)
# s 引用的是(1, 2, 3)这个key对应的value的地址
s = dict2[(1, 2, 3)]
s.append(8)
# 这里左边的s指向的时新的地址
s = s + [8, 9, 10]
print(dict2[(1, 2, 3)] + [8, 9, 10])
print(dict2)

del dict2['a']
print(dict2)
dict2.clear()
print(dict2)

# 已序列中的元素作为字典的key创建字典
print(dict1.fromkeys('abc'))
print(dict1.fromkeys(('A', 'B', 'C')))
dict3 = dict1.fromkeys([1, 2, 3, 4])
print(dict3)

# 字典的浅拷贝
dict4 = dict3.copy()
print(dict4)
dict4[1] = 'a'
print('dict3:' + str(dict3))
print('dict4:' + str(dict4))

print(1 in dict3)

print(dict3.items())
