#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 作者： RandyZhang
# 时间： 2018/6/8

from tkinter import *   # 导入Tkinter库
root = Tk()

li = ['C', 'python', 'php', 'html', 'sql', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']

listBox = Listbox(root)
listBox2 = Listbox(root)
for item in li:
    listBox.insert(0, item)

for item in movie:
    listBox2.insert(0, item)


listBox.pack()
listBox2.pack()

root.mainloop()
