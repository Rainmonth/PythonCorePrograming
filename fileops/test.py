# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# x = "a"
# y = "b"
# # 换行输出
# print(x)
# print(y)
#
# print('---------')
# # 不换行输出
# print(x),
# print(y),
#
# tuple1 = ('runoob', 786, 2.23, 'john', 70.2)
# tinytuple = (123, 'john')
#
# print(tuple1)  # 输出完整元组
# print(tuple1[0])  # 输出元组的第一个元素
# print(tuple1[1:3])  # 输出第二个至第三个的元素
# print(tuple1[2:])  # 输出从第三个开始至列表末尾的所有元素
# print(tinytuple * 2)  # 输出元组两次
# print(tuple1 + tinytuple)  # 打印组合的元组å
#
# tuple = ('runoob', 786, 2.23, 'john', 70.2)
# list = ['runoob', 786, 2.23, 'john', 70.2]
# # tuple[2] = 1000  # 元组中是非法应用
# print(list)
# list[2] = 1000  # 列表中是合法应用
# print(list)
# !/usr/bin/python
# -*- coding: UTF-8 -*-

# num = []
# i = 2
# for i in range(2, 100):
#     j = 2
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         num.append(i)
# print(num)

# i = 2
# while i < 100:
#     j = 2
#     while j <= (i / j):
#         if not (i % j):
#             break
#         j = j + 1
#     if j > i / j:
#         print(i, " 是素数")
#     i = i + 1
#
# print("Good bye!")


# list_2d = [[0 for i in range(5)] for i in range(5)]
# list_2d[0].append(1)
# list_2d[0].append(3)
# list_2d[0].append(5)
# list_2d[2].append(7)
# print(list_2d)
# print(len(list_2d))

# # 日期和时间
# import time_demo  # 引入时间
#
# # 获取时间戳
# ticks = time_demo.time_demo()
# print("当前时间戳为：", ticks)
#
# # 获取本地时间
# local_time = time_demo.localtime(time_demo.time_demo())
# print("本地时间元组为：", local_time)
#
# # 获取格式化时间
# local_time = time_demo.asctime(time_demo.localtime(time_demo.time_demo()))
# print("本地时间为：", local_time)
#
# # 自定义格式化
# print(time_demo.strftime("%Y-%m-%d %H:%M:%S", time_demo.localtime()))
#
# # 将格式化时间转化为时间戳
# a = "Mon May  8 14:27:08 2017"
# print(time_demo.mktime(time_demo.strptime(a, "%a %b %d %H:%M:%S %Y")))

# from utils.first_util import runoob1
# from utils.second_util import runoob2
# runoob1()
# runoob2()
# string = input("请输入：")
# print("你输入的内容是：", string)

fo = open("foo.txt", "r+")
print("文件名", fo.name)
print("是否已关闭", fo.closed)
# fo.write('www.rainmonth.cn!\nVery Good Site\n')
got_str = fo.read(20)
print("读取到的字符串：", got_str)
print("访问模式", fo.mode)
fo.close()
print("是否已关闭", fo.closed)
