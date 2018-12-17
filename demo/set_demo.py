#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 描述： 集合示例
# 作者： randy
# 时间： 2018/12/11 2:41 PM

# 集合的创建
set1 = {1, 2, 3, 4}
set2 = set('a')

# 创建一个空集合
empty_set = set()  # not empty_set = {}，这个操作是创建一个新字典

# 添加一个元素
empty_set.add('a')
print(empty_set)

# 批量增加元素
set1.update({'a', 'b', 'c'})
print(set1)
set2.update([1, 'b', 'd'])
print(set2)
set2.update(('abc', 'a', 1))
print(set2)
set2.clear()
set2.update(['a', 'c'], {'a', 'b', 1, 2}, (4, 5, 'c'))
print(set2)

# 移除元素
set3 = set('baidu', 'tecent', 'ali', 'jd')
set3.remove('baidu')
try:
    set3.remove('x')
except Exception as e:
    print(e)

set3.discard('x')
print(set3)
set3.pop()
print(set3)

s = set([3, 5, 9, 10])  # 创建一个数值集合，返回{3, 5, 9, 10}
t = set("Hello")  # 创建一个字符的集合，返回{'l', 'H', 'e', 'o'}
c = s - t
d = t - s
