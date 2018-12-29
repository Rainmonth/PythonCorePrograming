#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 描述： python adb 命令操作
# 作者： randy
# 时间： 2018/12/17 7:18 PM

import os

os.system('adb version')
os.system('adb devices')

# 获取屏幕的宽高
out = os.popen('adb shell wm size').read()
print(out)

# 调用WindowManager打印Window栈信息 adb shell dumpsys window windows
print(os.popen('adb shell dumpsys window windows').read())

# 查看指定包信息 adb shell dumpsys package com.hhdd.kada


# 查看电源信息 adb shell dumpsys power


# print(os.popen('adb shell dumpsys window windows |grep "mCurrentFocus"').read())

