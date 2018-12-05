#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 多线程示例（利用thread）

# import thread python3.x中不在使用thread了，将其改成了_thread，并且推荐使用threading
import _thread
from time import sleep, ctime


def loop0():
    print('start loop0 at: ', ctime())
    sleep(4)
    print('end loop0 at: ', ctime())


def loop1():
    print('start loop1 at: ', ctime())
    sleep(2)
    print('end loop1 at: ', ctime())


def main():
    print('starting at: ', ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    # 添加该代码是为了保证在子线程执行完之前主线程不回退出
    sleep(6)
    print('all done at: ', ctime())


if __name__ == '__main__':
    main()
