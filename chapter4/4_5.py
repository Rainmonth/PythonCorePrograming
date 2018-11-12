#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 多线程示例（使用threading——传递一个可执行的类对象来创建threading实例）

import threading
from time import sleep, ctime


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


loops = [14, 2, 8]


def loop(nloop, nsec):
    print(nloop, 'start at:', ctime())
    sleep(nsec)
    print(nloop, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))  # 传递一个函数
        threads.append(t)

    for i in nloops:
        threads[i].start()  # 开始所有线程

    for i in nloops:
        threads[i].join()  # 在启动线程终止之前一直挂起（等待所有子线程终止）

    print('all done at:', ctime())


if __name__ == '__main__':
    main()
