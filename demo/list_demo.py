#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 作者： RandyZhang
# 时间： 2017/8/23

# 序列的通用操作
list1 = [1, 'a', 2]
list2 = [3, 'b', 4]
# 列表索引
print(list1[-1])

list1[0] = 2
print(list1)
del list1[2]
print(list1)

print(len(list1))

print(list1 + list2)

# 列表拼接
for x in list1 + list2:
    print(x, end=' ')

# 列表重复
for y in list1 * 4:
    print(y, end=' ')

print(list1[-2])

print(tuple(list1))

list3 = list1.copy()
print(list3)
print(list3.pop())
print(list3)
list1.clear()
print(list1)

# 最大最小值，列表的类型需要统一
list4 = ['a', 'b', 'd', 'z', 'c']
list5 = [1, 6, 7, 9, 10, 22]

# 列表截取
print('列表截取' + str(list5[2:4]))
print('列表截取' + str(list5[2:]))

print('max:' + max(list4) + ', min:' + min(list4))
print('max:' + str(max(list5)) + ', min:' + str(min(list5)))

list4.reverse()
print(list4)

print(list4.sort())

# 列表嵌套
list6 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('列表嵌套:' + str(list6))
print('嵌套列表索引：' + str(list6[2][2]))

# 元组
tuple1 = 1, 2, 3
print('tuple1:' + str(tuple1))
tuple2 = (4, 5, 6)
print('tuple2:' + str(tuple2))

print('元组转换为列表:' + str(list(tuple1 + tuple2)))
print('元组最大值:' + str(max(tuple1 + tuple2)))
print('元组最小值:' + str(min(tuple1 + tuple2)))
print('元组长度:' + str(len(tuple1 + tuple2)))
print('元组截取:' + str((tuple1 + tuple2)[2:5]))

print('tuple1+tuple2:' + str(tuple1 + tuple2))
try:
    del tuple2
    print('tuple1+tuple2:' + str(tuple1 + tuple2))
except Exception as e:
    print(e)
