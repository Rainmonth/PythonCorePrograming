#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 描述： python adb 命令操作
# 作者： randy
# 时间： 2018/12/17 7:18 PM

import os
import math
import time


# os.system('adb version')
# os.system('adb devices')

# 获取屏幕的宽高
# out = os.popen('adb shell wm size').read()
# print(out)

# 调用WindowManager打印Window栈信息 adb shell dumpsys window windows
# print(os.popen('adb shell dumpsys window windows').read())


# 查看指定包信息 adb shell dumpsys package com.hhdd.kada


# 查看电源信息 adb shell dumpsys power


# print(os.popen('adb shell dumpsys window windows |grep "mCurrentFocus"').read())

def get_launch_activity(package_name):
    """
    通过aapt 获取制定包名的启动Activity
    :param package_name:  应用包名
    :return:
    """
    return ''


def screen_cap(save_path='/sdcard/', save_name='test.jpg', pull_to='/Users/randy/Downloads'):
    save_path = input("请输入要保存到的路径:")
    save_name = input("请输入要保存的名称:")
    pull_to = input("请输入要拉取到的位置:")

    os.system('adb shell screencap -p ' + str(save_path) + str(save_name))
    os.system('adb shell pull ' + str(save_path) + str(save_name) + ' ' + pull_to)


def is_app_installed(package_name):
    package_list = get_installed_package_list()
    return package_name in package_list


def get_installed_package_list():
    """
    获取安装的应用包名列表
    :return: 包名列表
    """
    package_output_str = str(os.popen('adb shell pm list package').read())
    package_list = package_output_str.replace('package:', '').split('\n')

    return package_list


def is_power_off():
    power_str = str(os.popen("adb shell dumpsys power|grep 'Display Power: state='").read())
    return 'OFF' in power_str


def unlock_phone():
    """
    解锁手机
    :return:
    """
    # 判断是否处于power off状态
    if is_power_off():
        os.system('adb shell input keyevent 3')
    # 进入密码输入页面
    os.system('adb shell input swipe 300 900 540 540 500')
    # 输入密码
    pwd = input("请输入密码:")
    os.system('adb shell input text ' + pwd)
    print('等待5秒')
    time.sleep(5)


def get_app_icon_location():
    print('获取APP图标的位置区域')
    print('获取区域之后，随机生成一个位于该区域的点')


def app_locate_and_open():
    print('定位并打开APP')
    x = 935
    y = 821
    os.system('adb shell input tap ' + str(x) + ' ' + str(y))
    print('等待4秒')
    time.sleep(4)


def enter_sign():
    print('进入通知页面')
    x = 724
    y = 765
    os.system('adb shell input tap ' + str(x) + ' ' + str(y))
    print('等待3秒')
    time.sleep(3)
    print('进入签到页面')
    x = 700
    y = 1600
    os.system('adb shell input tap ' + str(x) + ' ' + str(y))


def do_sign_in():
    print('开始签到')


def do_sign_out():
    print('开始签退')


def swipe():
    x1 = input('请输入起点x1坐标:')
    y1 = input('请输入起点y1坐标:')
    x2 = input('请输入终点x2坐标:')
    y2 = input('请输入终点y2坐标:')
    duration = input('请输入滑动时间(毫秒):')
    direct_swipe(x1, y1, x2, y2, duration)


def direct_swipe(x1, y1, x2, y2, time):
    try:
        int_x1 = int(x1)
        int_y1 = int(y1)
        int_x2 = int(x2)
        int_y2 = int(y2)
        int_time = int(time)
        if int_x1 < int_x2:
            print('从左往右划')
        else:
            print('从右往左划')
        dx = math.fabs(int_x1 - int_x2)
        dy = math.fabs(int_y1 - int_y2)

        print('滑动距离:' + str(math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))))
        os.system('adb shell input swipe ' + str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2) + ' ' + str(time))
    except Exception as e:
        print(e)


def auto_sign():
    # 如果处于锁屏页面，先解锁
    unlock_phone()
    # 找到相应的应用，打开
    app_locate_and_open()
    # 进入签到页面
    enter_sign()

    # 开始签到
    do_sign_in()


# adb shell input                                       查看input的帮助
# adb shell input tap x,y                               点击屏幕上坐标为(x,y)的点
# adb shell input swipe x1,y1,x2,y2,duration            从屏幕(x1,y1)滑动到(x2,y2)
# adb shell input swipe x1,y1,x1+1,y1+1 duration        模拟长按屏幕(x1,y1)这个点
# adb shell input text 'abc'                            模拟输入abc
# abd shell input keyevent KEY_EVENT_CODE               模拟键盘输入时间
# adb shell input keyevent --longpress KEY_EVENT_CODE   模拟长按KEY_EVENT_CODE键

if __name__ == '__main__':
    if is_app_installed('com.hhdd.kada'):
        print("已安装")
    else:
        print("未安装")

    # unlock_phone()
    # swipe()
    # direct_swipe(100, 200, 350, 630, 500)
    # app_locate_and_open()
    # enter_sign()
    # 开始签到
    # do_sign_in()
    # 一段时间后签退
    # do_sign_out()

    auto_sign()
